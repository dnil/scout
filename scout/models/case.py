# -*- coding: utf-8 -*-
"""

"main concept of MongoDB is embed whenever possible"
Ref: http://stackoverflow.com/questions/4655610#comment5129510_4656431
"""
from __future__ import absolute_import, unicode_literals
from datetime import datetime

from mongoengine import (
  DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField,
  IntField, ListField, ReferenceField, StringField
)

from .event import Event


class Individual(EmbeddedDocument):
  display_name = StringField()
  sex = StringField()
  phenotype = IntField()
  father = StringField()
  mother = StringField()
  individual_id = StringField()
  capture_kit = ListField(StringField())

  @property
  def sex_human(self):
    """Transform sex string into human readable form."""
    # pythonic switch statement
    return {
      '1': 'male',
      '2': 'female'
    }.get(self.sex, 'unknown')

  @property
  def phenotype_human(self):
    """Transform phenotype integer into human readable form."""
    # pythonic switch statement
    return {
      -9: 'missing',
       0: 'missing',
       1: 'unaffected',
       2: 'affected'
    }.get(self.phenotype, 'undefined')

  def __unicode__(self):
    return self.display_name


class PhenotypeTerm(EmbeddedDocument):
  id = StringField()
  feature = StringField()


class Case(Document):
  # This is the md5 string id for the family:
  case_id = StringField(primary_key=True, required=True)
  display_name = StringField(required=True)
  assignee = ReferenceField('User')
  individuals = ListField(EmbeddedDocumentField(Individual))
  databases = ListField(StringField())
  created_at = DateTimeField(default=datetime.now)
  updated_at = DateTimeField(default=datetime.now)
  last_updated = DateTimeField()
  suspects = ListField(ReferenceField('Variant'))
  synopsis = StringField(default='')
  status = StringField(default='inactive', choices=[
    'inactive', 'active', 'research', 'archived', 'solved'
  ])
  events = ListField(EmbeddedDocumentField(Event))
  gene_lists = ListField(StringField())
  gender_check = StringField(choices=['unconfirmed', 'confirm', 'deviation'],
                             default='unconfirmed')
  phenotype_terms = ListField(EmbeddedDocumentField(PhenotypeTerm))

  @property
  def hpo_genes(self):
    """Return the list of HGNC symbols that match annotated HPO terms."""
    return ['ANKRD11', 'PORCN', 'POR2']

  madeline_info = StringField()

  def __unicode__(self):
    return self.display_name
