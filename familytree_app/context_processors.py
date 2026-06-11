# /home/keyurjoshi/familytree_project/familytree_app/context_processors.py

from .models import FamilyMember, City, FamilyIdentification

def total_member_counts(request):
    """
    Context processor to calculate total family member counts.
    """
    total_family_members = FamilyMember.objects.count()
    total_males = FamilyMember.objects.filter(gender='M').count()
    total_females = FamilyMember.objects.filter(gender='F').count()

    return {
        'total_family_members': total_family_members,
        'total_males': total_males,
        'total_females': total_females,
    }

def combo_box_data(request):
    """
    Context processor to provide combo box data for surnames, cities, and family identifications.
    """
    # Fetch distinct surnames
    all_surnames = FamilyMember.objects.values_list('surname', flat=True).distinct()
    

    # Fetch distinct city and family identification IDs
    distinct_cities_ids = FamilyMember.objects.values_list('city', flat=True).distinct()
    distinct_family_identifications_ids = FamilyMember.objects.values_list('family_identification', flat=True).distinct()

    # Fetch related objects using the IDs
    cities = City.objects.filter(id__in=distinct_cities_ids)
    family_identifications = FamilyIdentification.objects.filter(id__in=distinct_family_identifications_ids)

    return {
        'cities': cities,
        'family_identifications': family_identifications,
        'all_surnames': sorted(set(all_surnames)),
    }
