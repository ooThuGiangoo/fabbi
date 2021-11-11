from django.contrib import admin

from Point.models import Point_spending_history, Points_package, Points_package_history, User_point
from Point.models import Follow, Gift, Gift_purchase_history, Gift_tipping_history, Ranking, Ranking_summary, Stamps_code, User_gift, User_stamp

# Register your models here.
admin.site.register(User_point)
admin.site.register(Points_package)
admin.site.register(Points_package_history)
admin.site.register(Point_spending_history)
admin.site.register(User_stamp)
admin.site.register(Gift)
admin.site.register(Gift_purchase_history)
admin.site.register(Gift_tipping_history)
admin.site.register(User_gift)
admin.site.register(Stamps_code)
admin.site.register(Follow)
admin.site.register(Ranking)
admin.site.register(Ranking_summary)

