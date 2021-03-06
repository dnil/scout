from copy import deepcopy
import pytest


@pytest.yield_fixture
def real_oldcase_database(real_panel_database, scout_config):
    # add case with old case id construct
    config_data = deepcopy(scout_config)
    config_data['family'] = '-'.join([config_data['owner'], config_data['family_name']])
    case_obj = real_panel_database.load_case(config_data)
    # add suspect and causative!
    institute_obj = real_panel_database.institute(case_obj['owner'])
    user_obj = real_panel_database.users()[0]
    variant_obj = real_panel_database.variants(case_obj['_id'])[0]
    real_panel_database.pin_variant(
        institute=institute_obj,
        case=case_obj,
        user=user_obj,
        link='',
        variant=variant_obj,
    )
    real_panel_database.mark_causative(
        institute=institute_obj,
        case=case_obj,
        user=user_obj,
        link='',
        variant=variant_obj,
    )
    # add ACMG evaluation
    real_panel_database.submit_evaluation(
        variant_obj=variant_obj,
        user_obj=user_obj,
        institute_obj=institute_obj,
        case_obj=case_obj,
        link='',
        criteria=[{'term': 'PS1'}, {'term': 'PM1'}],
    )
    # add comment on a variant
    real_panel_database.comment(
        institute=institute_obj,
        case=case_obj,
        user=user_obj,
        link='',
        variant=variant_obj,
        comment_level='specific',
    )
    yield {
        'adapter': real_panel_database,
        'variant': variant_obj,
        'case': real_panel_database.case(case_obj['_id']),
    }
