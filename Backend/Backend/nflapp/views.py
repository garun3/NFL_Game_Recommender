from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import redirect
from .models import Link
from .utils import get_game_recs, get_game_id, get_youtube_links

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MainView(TemplateView):
    template_name = 'main.html'

class SearchResultsView(ListView):
    model = Link
    template_name = 'results.html'
        
    def get_queryset(self):
        object_list = Link.objects.all
        return object_list

    def get_context_data(self, **kwargs):
        season = self.request.GET.get('season')
        week = self.request.GET.get('week')
        game = self.request.GET.get('game')
        num_games = self.request.GET.get('num_games')
        game_id, q = get_game_id(self, game, week, season)
        full = 0
        df, box_score_links = get_game_recs(self, game_id, int(num_games), 0)

        youtube_links = get_youtube_links(self, df)
        data = super().get_context_data(**kwargs)

        data['game_name'] = q
        data['df'] = zip(df, box_score_links, youtube_links)
        if full:
            data['header'] = []
        else:
            data['header'] = ['Week-Season', 'Winning Team', 'Losing Team', 'Home Score', 'Away Score', 'Box Score Link', 'Youtube Link']
        return data

    
