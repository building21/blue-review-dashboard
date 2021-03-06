from django.db import models
from django.urls import reverse

# Create your models here.

class Application(models.Model):
	FACULTY_CHOICES = (
		('Agricultural_Environmental_Sciences', 'Faculty of Agricultural and Environmental Sciences'),
		('Arts', 'Faculty of Arts'),
		('Continuing_Studies', 'School of Continuing Studies'),
		('Dentistry', 'Faculty of Dentistry'),
		('Education', 'Faculty of Education'),
		('Engineering', 'Faculty of Engineering'),
		('Law', 'Faculty of Law'),
		('Management', 'Desautels Faculty of Management'),
		('Medicine', 'Faculty of Medicine'),
		('Music', 'Schulich School of Music'),
		('Science', 'Faculty of Science'),
		('Other', 'Other')
		)

	COUNTRY_CHOICES = (
		('Afghanistan', 'Afghanistan'),
		('Albania', 'Albania'),
		('Algeria', 'Algeria'),
		('Andorra', 'Andorra'),
		('Angola', 'Angola'),
		('Anguilla', 'Anguilla'),
		('Antigua & Barbuda', 'Antigua & Barbuda'),
		('Argentina', 'Argentina'),
		('Armenia', 'Armenia'),
		('Australia', 'Australia'),
		('Austria', 'Austria'),
		('Azerbaijan', 'Azerbaijan'),
		('Bahamas', 'Bahamas'),
		('Bahrain', 'Bahrain'),
		('Bangladesh', 'Bangladesh'),
		('Barbados', 'Barbados'),
		('Belarus', 'Belarus'),
		('Belgium', 'Belgium'),
		('Belize', 'Belize'),
		('Benin', 'Benin'),
		('Bermuda', 'Bermuda'),
		('Bhutan', 'Bhutan'),
		('Bolivia', 'Bolivia'),
		('Bosnia & Herzegovina', 'Bosnia & Herzegovina'),
		('Botswana', 'Botswana'),
		('Brazil', 'Brazil'),
		('Brunei Darussalam', 'Brunei Darussalam'),
		('Bulgaria', 'Bulgaria'),
		('Burkina Faso', 'Burkina Faso'),
		('Burundi', 'Burundi'),
		('Cambodia', 'Cambodia'),
		('Cameroon', 'Cameroon'),
		('Canada', 'Canada'),
		('Cape Verde', 'Cape Verde'),
		('Cayman Islands', 'Cayman Islands'),
		('Central African Republic', 'Central African Republic'),
		('Chad', 'Chad'),
		('Chile', 'Chile'),
		('China', 'China'),
		('China - Hong Kong / Macau', 'China - Hong Kong / Macau'),
		('Colombia', 'Colombia'),
		('Comoros', 'Comoros'),
		('Congo', 'Congo'),
		('Congo, Democratic Republic of (DRC)', 'Congo, Democratic Republic of (DRC)'),
		('Costa Rica', 'Costa Rica'),
		('Croatia', 'Croatia'),
		('Cuba', 'Cuba'),
		('Cyprus', 'Cyprus'),
		('Czech Republic', 'Czech Republic'),
		('Denmark', 'Denmark'),
		('Djibouti', 'Djibouti'),
		('Dominica', 'Dominica'),
		('Dominican Republic', 'Dominican Republic'),
		('Ecuador', 'Ecuador'),
		('Egypt', 'Egypt'),
		('El Salvador', 'El Salvador'),
		('Equatorial Guinea', 'Equatorial Guinea'),
		('Eritrea', 'Eritrea'),
		('Estonia', 'Estonia'),
		('Ethiopia', 'Ethiopia'),
		('Fiji', 'Fiji'),
		('Finland', 'Finland'),
		('France', 'France'),
		('French Guiana', 'French Guiana'),
		('Gabon', 'Gabon'),
		('Gambia', 'Gambia'),
		('Georgia', 'Georgia'),
		('Germany', 'Germany'),
		('Ghana', 'Ghana'),
		('Great Britain', 'Great Britain'),
		('Greece', 'Greece'),
		('Grenada', 'Grenada'),
		('Guadeloupe', 'Guadeloupe'),
		('Guatemala', 'Guatemala'),
		('Guinea', 'Guinea'),
		('Guinea-Bissau', 'Guinea-Bissau'),
		('Guyana', 'Guyana'),
		('Haiti', 'Haiti'),
		('Honduras', 'Honduras'),
		('Hungary', 'Hungary'),
		('Iceland', 'Iceland'),
		('India', 'India'),
		('Indonesia', 'Indonesia'),
		('Iran', 'Iran'),
		('Iraq', 'Iraq'),
		('Israel and the Occupied Territories', 'Israel and the Occupied Territories'),
		('Italy', 'Italy'),
		('Ivory Coast (Cote d\'Ivoire)', 'Ivory Coast (Cote d\'Ivoire)'),
		('Jamaica', 'Jamaica'),
		('Japan', 'Japan'),
		('Jordan', 'Jordan'),
		('Kazakhstan', 'Kazakhstan'),
		('Kenya', 'Kenya'),
		('Korea, Democratic Republic of (North Korea)', 'Korea, Democratic Republic of (North Korea)'),
		('Korea, Republic of (South Korea)', 'Korea, Republic of (South Korea)'),
		('Kosovo', 'Kosovo'),
		('Kuwait', 'Kuwait'),
		('Kyrgyz Republic (Kyrgyzstan)', 'Kyrgyz Republic (Kyrgyzstan)'),
		('Laos', 'Laos'),
		('Latvia', 'Latvia'),
		('Lebanon', 'Lebanon'),
		('Lesotho', 'Lesotho'),
		('Liberia', 'Liberia'),
		('Libya', 'Libya'),
		('Liechtenstein', 'Liechtenstein'),
		('Lithuania', 'Lithuania'),
		('Luxembourg', 'Luxembourg'),
		('Macedonia, Republic of', 'Macedonia, Republic of'),
		('Madagascar', 'Madagascar'),
		('Malawi', 'Malawi'),
		('Malaysia', 'Malaysia'),
		('Maldives', 'Maldives'),
		('Mali', 'Mali'),
		('Malta', 'Malta'),
		('Martinique', 'Martinique'),
		('Mauritania', 'Mauritania'),
		('Mauritius', 'Mauritius'),
		('Mayotte', 'Mayotte'),
		('Mexico', 'Mexico'),
		('Moldova, Republic of', 'Moldova, Republic of'),
		('Monaco', 'Monaco'),
		('Mongolia', 'Mongolia'),
		('Montenegro', 'Montenegro'),
		('Montserrat', 'Montserrat'),
		('Morocco', 'Morocco'),
		('Mozambique', 'Mozambique'),
		('Myanmar/Burma', 'Myanmar/Burma'),
		('Namibia', 'Namibia'),
		('Nepal', 'Nepal'),
		('New Zealand', 'New Zealand'),
		('Nicaragua', 'Nicaragua'),
		('Niger', 'Niger'),
		('Nigeria', 'Nigeria'),
		('Norway', 'Norway'),
		('Oman', 'Oman'),
		('Pacific Islands', 'Pacific Islands'),
		('Pakistan', 'Pakistan'),
		('Panama', 'Panama'),
		('Papua New Guinea', 'Papua New Guinea'),
		('Paraguay', 'Paraguay'),
		('Peru', 'Peru'),
		('Philippines', 'Philippines'),
		('Poland', 'Poland'),
		('Portugal', 'Portugal'),
		('Puerto Rico', 'Puerto Rico'),
		('Qatar', 'Qatar'),
		('Reunion', 'Reunion'),
		('Romania', 'Romania'),
		('Russian Federation', 'Russian Federation'),
		('Rwanda', 'Rwanda'),
		('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
		('Saint Lucia', 'Saint Lucia'),
		('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
		('Samoa', 'Samoa'),
		('Sao Tome and Principe', 'Sao Tome and Principe'),
		('Saudi Arabia', 'Saudi Arabia'),
		('Senegal', 'Senegal'),
		('Serbia', 'Serbia'),
		('Seychelles', 'Seychelles'),
		('Sierra Leone', 'Sierra Leone'),
		('Singapore', 'Singapore'),
		('Slovak Republic (Slovakia)', 'Slovak Republic (Slovakia)'),
		('Slovenia', 'Slovenia'),
		('Solomon Islands', 'Solomon Islands'),
		('Somalia', 'Somalia'),
		('South Africa', 'South Africa'),
		('South Sudan', 'South Sudan'),
		('Spain', 'Spain'),
		('Sri Lanka', 'Sri Lanka'),
		('Sudan', 'Sudan'),
		('Suriname', 'Suriname'),
		('Swaziland', 'Swaziland'),
		('Sweden', 'Sweden'),
		('Switzerland', 'Switzerland'),
		('Syria', 'Syria'),
		('Tajikistan', 'Tajikistan'),
		('Tanzania', 'Tanzania'),
		('Thailand', 'Thailand'),
		('Netherlands', 'Netherlands'),
		('Timor Leste', 'Timor Leste'),
		('Togo', 'Togo'),
		('Trinidad & Tobago', 'Trinidad & Tobago'),
		('Tunisia', 'Tunisia'),
		('Turkey', 'Turkey'),
		('Turkmenistan', 'Turkmenistan'),
		('Turks & Caicos Islands', 'Turks & Caicos Islands'),
		('Uganda', 'Uganda'),
		('Ukraine', 'Ukraine'),
		('United Arab Emirates', 'United Arab Emirates'),
		('United States of America (USA)', 'United States of America (USA)'),
		('Uruguay', 'Uruguay'),
		('Uzbekistan', 'Uzbekistan'),
		('Venezuela', 'Venezuela'),
		('Vietnam', 'Vietnam'),
		('Virgin Islands (UK)', 'Virgin Islands (UK)'),
		('Virgin Islands (US)', 'Virgin Islands (US)'),
		('Yemen', 'Yemen'),
		('Zambia', 'Zambia'),
		('Zimbabwe', 'Zimbabwe')
		)

	email = models.EmailField(unique=True)
	date_commitment = models.BooleanField()
	name = models.CharField(max_length=256)
	faculty = models.CharField(max_length=35, choices=FACULTY_CHOICES)
	other_faculty = models.CharField(max_length=100, blank=True)
	project_name = models.CharField(max_length=1024)
	idea = models.TextField()
	fit_for_blue = models.TextField()
	media_link = models.CharField(max_length=1024)
	country = models.CharField(max_length=128, choices=COUNTRY_CHOICES)
	year = models.CharField(max_length=50)
	valid = models.BooleanField()
		
	# Metadata
	class Meta(object):
		ordering = ['id']
		permissions = (("can_upload", "Can upload applications to the database"),)

	# Functions
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('application-detail', args=[str(self.id)])

	def __str__(self):
		return "[Application: %s]" % (self.name)

	def clean(self):
		pass
