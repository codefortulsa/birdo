from rest_framework.routers import DefaultRouter

from .views import BirdViewSet, PermutationViewSet, PermutationTypeViewSet


router = DefaultRouter()

router.register(r'birds', BirdViewSet, base_name='bird')
router.register(r'permutations', PermutationViewSet, base_name='permutation')
router.register(r'permutation-types', PermutationTypeViewSet, base_name='permutation-type')


urlpatterns = router.urls
