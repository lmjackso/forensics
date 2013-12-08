import parser


def home(request):
  context = {}
  metadata_map(PROJECT_ROOT)
  return render(request, 'DFA/test.html', context)