from django.db import models
from django.utils import timezone

'''
These models were coded without any afterthought as to the program structure or functionality. Trying to learn :)
'''


'''
A company which users are able to contact in order to obtain revenue.
'''
class Company(models.Model):
    name = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    #is_closed = 0   # Is the company (incl. contact information) freely available to all users
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "companies"
    
'''
A model for a contact. A contact is a person related to one or more companies through the model Contact_Information.
'''
class Contact(models.Model):
    name = models.CharField(max_length=64)
    #is_member_of_association = 0    # If the contact is or has been a member of the association which is using the CRM (e.g. TF)
    associated_companies = models.ManyToManyField(Company, through='ContactInformation')
    
    #This as ManyToManyField doesn't support list_display
    def associated_company_names(self):
        return ', '.join([ac.name for ac in self.associated_companies.all()])
    associated_company_names.short_description = "Associated companies"
    
    def __unicode__(self):
        return u'%s' % (self.name)



class ContactInformation(models.Model):
    company = models.ForeignKey(Company)
    contact = models.ForeignKey(Contact)
    title = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=32)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.title, self.email, self.phone_number)

    class Meta:
        verbose_name_plural = "contact information"