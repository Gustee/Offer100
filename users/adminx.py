import xadmin
from .models import *

xadmin.site.register(HR)
xadmin.site.register(Candidate)
xadmin.site.register(EmailVerifyRecord)