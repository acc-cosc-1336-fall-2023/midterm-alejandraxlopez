#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_assessment_value(value):
    assessmentval = value * 0.6
    return assessmentval

def get_tax_assessed(assessment_value):
    rate = assessment_value / 100 * (0.72)
    tax = round(rate, 2)
    return tax

