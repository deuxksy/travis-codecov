from django.test import TestCase

# Create your tests here.
class TemplateKoreanTestCase(TestCase):
    def setUp(self):
        pass

    def test_test(self):
        self.assertEqual(1, 1)

    def test_korean_proofread_tag(self):
        from django.template import  Context, Template
        rendered = Template(
            '{% load proofread %}'
            '{{ string|proofread }}'
        ).render(Context({
            'string' : '나(은)는 밥(을)를 먹고 싶다',
        }))
        self.assertEqual(rendered, '나는 밥을 먹고 싶다')