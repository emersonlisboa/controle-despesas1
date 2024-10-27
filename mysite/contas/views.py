from django.shortcuts import render

# Create your views here.
class ContasListView(ListView):
    model = Conta
    template_name = 'contas/lista_contas.html'
    context_object_name = 'contas'

class ContaDetailView(DetailView):
    model = Conta
    template_name = 'contas/detalhe_conta.html'
    context_object_name = 'conta'

class ContaCreateView(CreateView):
    model = Conta
    template_name = 'contas/criar_conta.html'
    fields = ['nome', 'valor', 'tipo']
    success_url = reverse_lazy('contas:lista_contas')

class ContaUpdateView(UpdateView):
    model = Conta
    template_name = 'contas/atualizar_conta.html'
    fields = ['nome', 'valor', 'tipo']
    success_url = reverse_lazy('contas:lista_contas')'    
   
