import 'package:flutter/material.dart';

class Conversora extends StatefulWidget {
  const Conversora({super.key});

  @override
  _ConversoraState createState() => _ConversoraState();
}

class _ConversoraState extends State<Conversora> {
  final TextEditingController _controllerNumEmpregados = TextEditingController();
  final TextEditingController _controllerCustoBicicleta = TextEditingController();
  final TextEditingController _controllerNumBicicletasVendidas = TextEditingController();
  String _resultadoConv = '';

  final double salarioMinimo = 1500;
  final double acrescimoBicicleta = 0.50;
  final double comissao = 0.15;

  void _converter() {
    final double? numEmpregados = double.tryParse(_controllerNumEmpregados.text);
    final double? custoBicicleta = double.tryParse(_controllerCustoBicicleta.text);
    final double? numBicicletasVendidas = double.tryParse(_controllerNumBicicletasVendidas.text);

    if (numEmpregados != null &&
        custoBicicleta != null &&
        numBicicletasVendidas != null) {
      final double salarioComissao = salarioMinimo + (salarioMinimo * comissao);
      final double salarioFinalEmpregado = salarioComissao * numEmpregados;
      final double precoBicicletaVenda = custoBicicleta + (custoBicicleta * acrescimoBicicleta);
      final double receitaLoja = precoBicicletaVenda * numBicicletasVendidas;
      final double custoTotalBicicletas = custoBicicleta * numBicicletasVendidas;
      final double lucroLoja = receitaLoja - custoTotalBicicletas - salarioFinalEmpregado;

      setState(() {
        _resultadoConv = '''
Salário Final por Empregado: R\$ ${salarioFinalEmpregado.toStringAsFixed(2)}
Receita da Loja: R\$ ${receitaLoja.toStringAsFixed(2)}
Lucro Final da Loja: R\$ ${lucroLoja.toStringAsFixed(2)}
        ''';
      });
    } else {
      setState(() {
        _resultadoConv = 'Por favor, insira valores válidos para todos os campos.';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: false,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Conversora'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextField(
                controller: _controllerNumEmpregados,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: 'Número de Empregados:',
                ),
              ),
              TextField(
                controller: _controllerCustoBicicleta,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: 'Custo da Bicicleta:',
                ),
              ),
              TextField(
                controller: _controllerNumBicicletasVendidas,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: 'Número de Bicicletas Vendidas:',
                ),
              ),
              const SizedBox(height: 32),
              FilledButton(onPressed: _converter, child: const Text('Calcular')),
              const SizedBox(height: 16),
              Text(
                _resultadoConv,
                style: const TextStyle(fontSize: 16),
                textAlign: TextAlign.left,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
