from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class MonModele(models.Model):
    """Modèle simple démontrant les bonnes pratiques Odoo V18"""
    
    _name = 'mon.modele'
    _description = 'Mon Modèle Simple'
    _order = 'name'
    _rec_name = 'name'
    
    # Champs de base
    name = fields.Char(
        string='Nom',
        required=True,
        help='Nom de l\'enregistrement'
    )
    
    description = fields.Text(
        string='Description',
        help='Description détaillée'
    )
    
    active = fields.Boolean(
        string='Actif',
        default=True,
        help='Décochez pour archiver l\'enregistrement'
    )
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmé'),
        ('done', 'Terminé'),
        ('cancelled', 'Annulé')
    ], string='État', default='draft', required=True)
    
    priority = fields.Selection([
        ('0', 'Faible'),
        ('1', 'Normal'),
        ('2', 'Élevé'),
        ('3', 'Urgent')
    ], string='Priorité', default='1')
    
    date_creation = fields.Datetime(
        string='Date de création',
        default=fields.Datetime.now,
        readonly=True
    )
    
    derniere_execution = fields.Datetime(
        string='Dernière exécution',
        readonly=True
    )
    
    succes = fields.Integer(
        string='Succès',
        default=0,
        readonly=True
    )
    
    erreurs = fields.Integer(
        string='Erreurs',
        default=0,
        readonly=True
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Utilisateur responsable',
        default=lambda self: self.env.user
    )
    
    # Champ calculé
    display_name_custom = fields.Char(
        string='Nom d\'affichage',
        compute='_compute_display_name_custom',
        store=True
    )
    
    @api.depends('name', 'state')
    def _compute_display_name_custom(self):
        """Calcule le nom d'affichage personnalisé"""
        for record in self:
            if record.name and record.state:
                record.display_name_custom = f"{record.name} ({dict(record._fields['state'].selection)[record.state]})"
            else:
                record.display_name_custom = record.name or ''
    
    @api.constrains('name')
    def _check_name_length(self):
        """Valide que le nom a une longueur minimale"""
        for record in self:
            if record.name and len(record.name.strip()) < 3:
                raise ValidationError("Le nom doit contenir au moins 3 caractères.")
    
    @api.onchange('priority')
    def _onchange_priority(self):
        """Met à jour l'état selon la priorité"""
        if self.priority == '3':  # Urgent
            return {
                'warning': {
                    'title': 'Priorité urgente',
                    'message': 'Cet enregistrement a été marqué comme urgent.'
                }
            }
    
    def action_confirm(self):
        """Confirme l'enregistrement"""
        self.ensure_one()
        if self.state == 'draft':
            self.state = 'confirmed'
            _logger.info(f"Enregistrement {self.name} confirmé par {self.env.user.name}")
        return True
    
    def action_done(self):
        """Marque l'enregistrement comme terminé"""
        self.ensure_one()
        if self.state == 'confirmed':
            self.state = 'done'
            _logger.info(f"Enregistrement {self.name} terminé par {self.env.user.name}")
        return True
    
    def action_cancel(self):
        """Annule l'enregistrement"""
        self.ensure_one()
        if self.state in ['draft', 'confirmed']:
            self.state = 'cancelled'
            _logger.info(f"Enregistrement {self.name} annulé par {self.env.user.name}")
        return True
    
    def action_reset_to_draft(self):
        """Remet l'enregistrement en brouillon"""
        self.ensure_one()
        self.state = 'draft'
        return True
    
    def action_draft(self):
        """Alias pour action_reset_to_draft (compatibilité vue)"""
        return self.action_reset_to_draft() 