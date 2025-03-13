import 'package:flutter/material.dart';

class ModButton extends StatelessWidget {
  final String nome;

  const ModButton({super.key, required this.nome});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
          onPressed: () {
            print(nome);
          },
          child: Text(nome),
        ),
      ],
    );
  }
}
