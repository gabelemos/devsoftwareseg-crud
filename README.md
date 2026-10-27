# 🏋️ Sistema de Gestão de Academia

Este projeto é desenvolvido para a disciplina de **Desenvolvimento de Software Seguro** (4º Período) da **Unifavip Wyden**, sob orientação da professora **Franciely**.

O objetivo é criar uma solução centralizada, organizada e segura para o gerenciamento de academias, garantindo controle total sobre as operações e protegendo os dados de cada usuário.

---

## 🔐 Níveis de Acesso

O sistema foi desenhado com foco em controle de permissões, dividindo os usuários em três perfis principais:

### 👑 Administrador
*Responsável pelo gerenciamento geral e integridade do sistema.*

**Poderá ver e gerenciar:**
- Cadastro de alunos, professores e usuários.
- Planos, treinos e informações gerais da academia.
- Logs de auditoria (ações realizadas no sistema).

**Poderá realizar:**
- CRUD completo (Cadastrar, Alterar, Excluir) de usuários, alunos e professores.
- Consultas avançadas de dados operacionais.

---

### 🏋️ Professor
*Acesso focado no acompanhamento técnico e pedagógico.*

**Poderá ver:**
- Seus alunos, dados básicos e planos.
- Informações de treinos sob sua responsabilidade.

**Poderá realizar:**
- Cadastro, consulta e alteração de treinos.
- Atualização de dados de acompanhamento dos alunos.

*(🚫 Não possui acesso a funções de administração ou exclusão de usuários).*

---

### 👤 Aluno
*Acesso limitado, focado na jornada individual.*

**Poderá ver:**
- Seus próprios dados cadastrais e de matrícula.
- Seu plano atual e seu treino designado.

**Poderá realizar:**
- Consulta de suas informações pessoais e rotina de exercícios.

*(🚫 Não possui privilégios de alteração de treinos ou acesso a dados de terceiros).*

---

## 🚀 Roadmap de Desenvolvimento

Atualmente, o projeto encontra-se em fase de **prototipagem (CLI)**, mas evoluirá para oferecer:

*   💾 **Persistência de Dados:** Integração com banco de dados para segurança e escalabilidade.
*   🖥️ **Interface Gráfica:** Criação de um ambiente intuitivo para os usuários.
*   🛡️ **Segurança em Software:** Implementação de boas práticas de autenticação, autorização e proteção de dados, conforme os princípios da disciplina.

---
*Desenvolvido por Gabriel Lemos e Emerson Júnior, Análise e Desenvolvimento de Sistemas - Unifavip Wyden.*
