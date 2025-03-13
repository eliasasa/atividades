import 'package:flutter/material.dart';

class ProfileInfo extends StatelessWidget {
  final String nome;
  final String url;

  const ProfileInfo({super.key, required this.nome, required this.url});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        SizedBox(
          height: 48,
          width: 48,
          child: ClipOval(
            child: Image.network(url, fit: BoxFit.cover,),
          ),
        ),
        Text(nome),
      ],
    );
  }
}
