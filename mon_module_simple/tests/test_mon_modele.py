from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMonModele(TransactionCase):
    """Tests pour le modèle Mon Modèle"""

    def setUp(self):
        """Configuration initiale des tests"""
        super().setUp()
        self.MonModele = self.env['mon.modele']
        self.test_user = self.env.ref('base.user_demo')

    def test_create_mon_modele(self):
        """Test de création d'un enregistrement"""
        modele = self.MonModele.create({
            'name': 'Test Modèle',
            'description': 'Description de test',
            'priority': '1'
        })
        
        self.assertTrue(modele.id)
        self.assertEqual(modele.name, 'Test Modèle')
        self.assertEqual(modele.state, 'draft')
        self.assertTrue(modele.active)
        self.assertEqual(modele.user_id, self.env.user)

    def test_name_constraint(self):
        """Test de la contrainte sur la longueur du nom"""
        with self.assertRaises(ValidationError):
            self.MonModele.create({
                'name': 'AB',  # Trop court
                'description': 'Test'
            })

    def test_compute_display_name_custom(self):
        """Test du champ calculé display_name_custom"""
        modele = self.MonModele.create({
            'name': 'Test Compute',
            'state': 'confirmed'
        })
        
        expected_display = 'Test Compute (Confirmé)'
        self.assertEqual(modele.display_name_custom, expected_display)

    def test_action_confirm(self):
        """Test de l'action de confirmation"""
        modele = self.MonModele.create({
            'name': 'Test Confirm',
            'state': 'draft'
        })
        
        result = modele.action_confirm()
        self.assertTrue(result)
        self.assertEqual(modele.state, 'confirmed')

    def test_action_done(self):
        """Test de l'action de finalisation"""
        modele = self.MonModele.create({
            'name': 'Test Done',
            'state': 'confirmed'
        })
        
        result = modele.action_done()
        self.assertTrue(result)
        self.assertEqual(modele.state, 'done')

    def test_action_cancel(self):
        """Test de l'action d'annulation"""
        modele = self.MonModele.create({
            'name': 'Test Cancel',
            'state': 'draft'
        })
        
        result = modele.action_cancel()
        self.assertTrue(result)
        self.assertEqual(modele.state, 'cancelled')

    def test_action_reset_to_draft(self):
        """Test de remise en brouillon"""
        modele = self.MonModele.create({
            'name': 'Test Reset',
            'state': 'confirmed'
        })
        
        result = modele.action_reset_to_draft()
        self.assertTrue(result)
        self.assertEqual(modele.state, 'draft')

    def test_onchange_priority(self):
        """Test de l'onchange sur la priorité"""
        modele = self.MonModele.new({
            'name': 'Test Priority',
            'priority': '3'  # Urgent
        })
        
        result = modele._onchange_priority()
        self.assertIsInstance(result, dict)
        self.assertIn('warning', result)

    def test_default_values(self):
        """Test des valeurs par défaut"""
        modele = self.MonModele.create({
            'name': 'Test Defaults'
        })
        
        self.assertEqual(modele.state, 'draft')
        self.assertEqual(modele.priority, '1')
        self.assertTrue(modele.active)
        self.assertTrue(modele.date_creation)

    def test_search_and_filtering(self):
        """Test des recherches et filtres"""
        # Créer des enregistrements de test
        modele1 = self.MonModele.create({
            'name': 'Modèle Actif',
            'state': 'draft',
            'active': True
        })
        
        modele2 = self.MonModele.create({
            'name': 'Modèle Inactif',
            'state': 'done',
            'active': False
        })
        
        # Test recherche par nom
        results = self.MonModele.search([('name', 'ilike', 'Actif')])
        self.assertIn(modele1, results)
        self.assertNotIn(modele2, results)
        
        # Test filtre actifs
        actifs = self.MonModele.search([('active', '=', True)])
        self.assertIn(modele1, actifs)
        self.assertNotIn(modele2, actifs) 