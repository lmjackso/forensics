import parser


def home(request):
  context = {}
  map = parse_map_from_directory(dir)
  return render(request, 'DFA/test.html', context)