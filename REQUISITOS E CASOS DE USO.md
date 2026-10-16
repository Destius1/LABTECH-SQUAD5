# Requisitos — Repertório dos Cursos de TI (MVP / TCC)

> Documento vivo da Fase 1 (Concepção). Atualizado incrementalmente durante a entrevista.

## 1. Problema
O acervo de TCCs dos cursos de TI é difícil de usar e de manter:
- A banca não consegue pesquisar na aba atual para encontrar TCCs.
- Estudantes que querem apenas um arquivo específico acabam baixando o TCC inteiro.
- TCCs sem identificadores se perdem, e os mentores precisam rolar a lista inteira para achá-los.
- Há TCCs vazios, sem conteúdo, apenas ocupando espaço sem necessidade.
- Os TCCs mais novos se perdem: às vezes vão parar no fim da lista por causa do título.

**Situação atual**: os TCCs são organizados na hierarquia curso > ano > semestre > turma. Os que não têm identificadores são colocados no nível do curso ou ficam em uma lista de links para drives, sem filtros.

## 2. Objetivos
Cada dor do problema vira um objetivo do MVP.

| # | Objetivo | Indicador |
|---|---|---|
| OBJ-01 | Permitir que a banca e os mentores encontrem um TCC por orientador, curso, ano, semestre e tecnologias. | Um avaliador encontra um TCC conhecido usando só a pesquisa e os filtros, sem percorrer a lista inteira. |
| OBJ-02 | Permitir o download de uma parte específica do TCC, sem baixar o restante. | O usuário baixa só o arquivo que quer, em uma única ação, sem receber o restante do TCC. |
| OBJ-03 | Garantir que todo TCC novo tenha curso, ano, semestre, turma, orientador, título e tecnologias. | 100% dos TCCs enviados pelo repertório com todos os campos preenchidos (RF-07). |
| OBJ-04 | Garantir que todo TCC novo tenha ao menos a monografia (PDF) e a autoria. | 100% dos TCCs enviados pelo repertório com os dois arquivos (RF-07). |
| OBJ-05 | Evitar que os TCCs mais novos se percam no fim da lista por causa do título. | Na lista padrão, os TCCs mais recentes (ano e semestre) aparecem primeiro (RN-15). |

## 3. Stakeholders
| Stakeholder | Perfil no sistema | Interesse |
|---|---|---|
| Estudantes (autores dos TCCs) | Estudante | Enviar o próprio TCC, corrigi-lo e consultar/baixar outros TCCs. |
| Banca avaliadora | Avaliador | Encontrar TCCs pela pesquisa e baixar as partes que precisa. |
| Mentores (professores orientadores) | Avaliador | Encontrar TCCs sem percorrer a lista inteira; o mentor de um semestre pode integrar a banca em outro. |
| Coordenação do curso de TI (uma só, para todos os cursos de TI) | Administrador | Manter o acervo organizado: cadastra matrículas e avaliadores e exclui TCCs vazios ou indevidos, de qualquer curso. |
| Professor orientador do TCC | _(não usa o sistema como perfil)_ | Aprova o MVP: valida os requisitos e a modelagem de dados. |

## 4. Escopo
- Aplicação web, em formato de MVP (produto mínimo viável), desenvolvida como TCC.
- Perfis de acesso: **estudante** (login por matrícula e senha; envia, pesquisa e baixa TCCs), **administrador** (login independente) e **avaliador** (perfil único que reúne banca e mentores; login próprio, diferente dos outros dois; pesquisa e baixa TCCs).
- O administrador cadastra manualmente as matrículas dos estudantes e os avaliadores.
- O estudante, depois de fazer login com a matrícula, envia o próprio TCC ao repertório.
- Um TCC de TI é composto por partes, que podem ser baixadas separadamente:
  - **Obrigatórias**: monografia (PDF) e autoria (arquivo anexado).
  - **Opcionais**: executável, código-fonte (.yml), apresentação de slides e disclaimer.
- A pesquisa de TCCs permite buscar pelo **nome do orientador**, combinada com filtros de **curso, ano, semestre e tecnologias/frameworks**. A lista de resultados vem, por padrão, com os **mais recentes primeiro** (por ano e semestre).
- A **turma** é registrada no TCC pelo estudante no envio, mas não é filtro de pesquisa.
- No envio, o estudante preenche obrigatoriamente: curso, ano, semestre, turma, nome do orientador, título do TCC e tecnologias/frameworks utilizados.
- O download é **por parte**: o usuário baixa apenas o arquivo que quer (monografia, slides, executável etc.). Não há download do TCC completo de uma vez.
- Depois do envio, o estudante edita o próprio TCC (não o exclui) e o administrador exclui qualquer TCC (não edita).
- O sistema envia dados para um MongoDB existente.

## 5. Fora do escopo
- Publicação do sistema na internet e a meta de disponibilidade em horário comercial (RNF-05): a entrega de 23/11/2026 roda só em computador local, para demonstração ao orientador.
- Cadastro de administradores pelo sistema (as contas são criadas pela equipe antes da entrega).
- Recuperação automática de senha por e-mail.
- Versionamento de TCCs (histórico de versões); a edição substitui o conteúdo anterior.
- Edição de TCCs pelo administrador e exclusão do próprio TCC pelo estudante.
- Resumo, palavras-chave e banca como metadados do TCC, e a busca por palavras-chave.
- Notificação por e-mail (o resultado do envio aparece na tela).
- Visibilidade configurável por arquivo (público, só participantes e banca, privado).
- Compilação e execução do código dos TCCs em ambiente isolado (o sistema só guarda o executável e o código-fonte).
- Download do TCC completo em um único arquivo.
- Integração automática com o sistema da faculdade (API ou acesso direto ao banco) para validar matrículas.
- Importação de matrículas por arquivo (CSV/planilha).

## 6. Personas
| Persona | Quem é | O que precisa fazer | Dor atual |
|---|---|---|---|
| Estudante | Autor de TCC de um curso de TI; entra com matrícula e senha. | Enviar o próprio TCC com os dados e arquivos obrigatórios, corrigi-lo e consultar ou baixar outros TCCs. | Baixa o TCC inteiro quando só queria um arquivo; TCCs sem identificadores se perdem. |
| Avaliador | Membro da banca ou mentor (professor); entra com nome de usuário e senha. | Encontrar um TCC pelo orientador, curso, ano, semestre e tecnologias e baixar a parte que precisa. | Não consegue pesquisar; rola a lista inteira; os TCCs mais novos ficam no fim da lista. |
| Administrador | Membro da coordenação do curso de TI. | Cadastrar matrículas e avaliadores, redefinir senhas de estudantes e excluir TCCs indevidos. | TCCs vazios e sem identificadores ocupam espaço e bagunçam o acervo. |

## 7. Casos de uso
| ID | Caso de uso | Ator | Requisitos |
|---|---|---|---|
| UC-01 | Fazer login | Estudante, avaliador, administrador | RF-01, RF-02, RF-03 |
| UC-02 | Definir a senha no primeiro acesso | Estudante, avaliador | RF-15 |
| UC-03 | Cadastrar matrículas | Administrador | RF-04 |
| UC-04 | Cadastrar avaliadores | Administrador | RF-05 |
| UC-05 | Redefinir a senha de um estudante | Administrador | RF-16 |
| UC-06 | Enviar TCC | Estudante | RF-06, RF-07 |
| UC-07 | Editar o próprio TCC | Estudante | RF-08 |
| UC-08 | Excluir TCC | Administrador | RF-09 |
| UC-09 | Pesquisar TCCs | Estudante, avaliador, administrador | RF-10 |
| UC-10 | Visualizar um TCC e suas partes | Estudante, avaliador, administrador | RF-11, RF-14 |
| UC-11 | Baixar uma parte do TCC | Estudante, avaliador, administrador | RF-12 |

## 8. Requisitos funcionais
| ID | Descrição | Critério de aceite | Prioridade |
|---|---|---|---|
| RF-01 | O estudante faz login informando a matrícula e a senha. | Matrícula cadastrada pelo administrador com senha correta dá acesso; matrícula não cadastrada ou senha incorreta é recusada com mensagem. | Must |
| RF-02 | O administrador faz login com credenciais próprias, independentes da matrícula. | Credenciais válidas dão acesso ao perfil de administrador; inválidas são recusadas. | Must |
| RF-03 | O avaliador (banca e mentores) faz login com nome de usuário e senha. | Avaliador cadastrado pelo administrador, com nome de usuário e senha corretos, tem acesso; credenciais inválidas são recusadas. | Must |
| RF-04 | O administrador cadastra as matrículas dos estudantes. | Após o cadastro, o estudante consegue fazer login com aquela matrícula. | Must |
| RF-05 | O administrador cadastra os avaliadores, informando o nome e criando o nome de usuário de cada um. | Após o cadastro, o avaliador define a senha no primeiro acesso e consegue entrar; não existe autocadastro. | Must |
| RF-06 | O estudante envia o próprio TCC com as informações obrigatórias (curso, ano, semestre, turma, nome do orientador, título e tecnologias/frameworks) e as partes do TCC. | O TCC fica disponível no repertório; partes obrigatórias: monografia (PDF) e autoria (arquivo); opcionais: executável, código-fonte (.yml), slides e disclaimer. | Must |
| RF-07 | O sistema valida o envio do TCC. | Envio sem algum campo obrigatório, sem a monografia ou sem o arquivo de autoria é recusado com indicação do que falta; arquivo acima de 50 MB é recusado. O resultado do envio (sucesso ou falha) aparece na tela. | Must |
| RF-08 | O estudante edita o próprio TCC depois de enviado. | As alterações aparecem na pesquisa e no download; as mesmas validações do envio se aplicam. | Should |
| RF-09 | O administrador exclui qualquer TCC. | O TCC excluído deixa de aparecer na pesquisa e no download. | Should |
| RF-10 | Estudantes e avaliadores pesquisam TCCs pelo nome do orientador, com filtros de curso, ano, semestre e tecnologias/frameworks. | A busca retorna só os TCCs que atendem aos critérios informados; a turma não é filtro; a busca por palavras-chave não existe; os resultados vêm por padrão ordenados do mais recente para o mais antigo (ano e semestre), e não por título. | Must |
| RF-11 | O usuário visualiza um TCC e a lista das suas partes. | Aparecem as informações do TCC e quais partes existem para baixar. | Must |
| RF-12 | O usuário baixa uma parte do TCC individualmente. | Baixa-se apenas o arquivo escolhido; não há download do TCC completo. | Must |
| RF-13 | O sistema registra logs de ações críticas (criação, edição e exclusão de TCCs) associados ao usuário logado e ao horário. | Cada ação crítica gera um registro com usuário, ação, TCC afetado e data/hora. _(origem: rascunho de referência, RF10)_ | Could |
| RF-14 | O usuário pré-visualiza a monografia (PDF) diretamente no navegador, sem baixar o arquivo. | A monografia abre na tela do navegador; o download continua disponível por parte. _(origem: rascunho de referência, RF11)_ | Could |
| RF-15 | No primeiro acesso, o estudante e o avaliador definem a senha da própria conta. | Estudante com matrícula cadastrada, ou avaliador cadastrado, que ainda não tem senha é levado a criar uma; depois disso o login exige identificador e senha. | Must |
| RF-16 | O administrador redefine a senha de um estudante que a esqueceu. | Após a redefinição, o estudante entra com a matrícula e cria uma nova senha, pelo mesmo fluxo do primeiro acesso (RF-15). | Should |

### 8.1 Decisões sobre o rascunho de referência
Itens do PDF "Requisitos do sistema" que conflitavam com o que já havia sido decidido ou ampliavam o escopo. Todos já têm decisão.

| Origem | Proposta | Relação com o que já decidimos | Recomendação | Decisão |
|---|---|---|---|---|
| RF04, RNF01, RNF02 | Compilar/executar o código dos TCCs em ambiente isolado (Docker/sandbox, timeout 30 s, 512 MB, sem rede) | Funcionalidade nova e grande; não resolve nenhuma das 4 dores do problema. O executável é só uma parte opcional guardada. | Fora do MVP (registrar como evolução futura) | **Decidido: fora do MVP** |
| RF01 | Login integrado ao sistema de RGM da UDF | Conflita com a decisão de cadastro manual das matrículas pelo administrador | Manter cadastro manual no MVP; integração como evolução futura | **Mantido o cadastro manual (decisão anterior); integração com o RGM fica como evolução futura** |
| RF03, RNF03 | Arquivos em Object Storage (compatível com S3), até 40 MB, em ZIP | Conflita com a decisão de guardar arquivos no MongoDB (50 MB, PDF e demais formatos) | Decidir onde os arquivos ficam antes da modelagem | **Decidido: arquivos no MongoDB (GridFS), até 50 MB; sem Object Storage** |
| RF08 | Visibilidade por arquivo: público / só participantes e banca / privado | Não decidido; afeta quem vê e baixa cada parte | Avaliar, pode ser útil para executável e código-fonte | **Decidido: sem controle por arquivo** |
| RF07 | Notificação por e-mail de sucesso/falha no envio | O sistema não coleta e-mail do estudante (login por matrícula) | Só entra se houver campo de e-mail; senão, mensagem na tela | **Decidido: sem e-mail; resultado na tela** |
| RF09 | Metadados extras no envio: resumo, banca, palavras-chave, tecnologias/frameworks | Nossos campos obrigatórios são curso, ano, semestre, turma, orientador e título | Avaliar palavras-chave e resumo; os demais aumentam o atrito no envio | **Decidido: entra só tecnologias/frameworks (obrigatório); sem resumo, palavras-chave nem banca** |
| RF02 | Pesquisa também por palavras-chave e título | Decidimos orientador + curso, ano e semestre | Depende de decidir as palavras-chave no envio | **Decidido: sem busca por palavras-chave (não são coletadas); filtro por tecnologias/frameworks entra; busca por título não entra** |
| RF06 | Administrador também adiciona e altera dados de TCCs | Resolve a dúvida aberta se o administrador também edita | Sim, acrescentar ao RF-08 | **Decidido: o administrador só exclui, não edita; o estudante não exclui** |
| RF12 | Versionamento: novas versões do TCC com histórico | Hoje o estudante só edita (sobrescreve) | Evolução futura; no MVP, edição simples | **Decidido: sem versionamento no MVP; a edição substitui o conteúdo anterior** |

## 9. Requisitos não funcionais
| ID | Categoria | Descrição |
|---|---|---|
| RNF-01 | Conformidade (LGPD) | Dados pessoais de estudantes e professores são tratados conforme a LGPD, com termo de consentimento para publicação dos trabalhos no repertório. _(origem: rascunho de referência, RNF04)_ |
| RNF-02 | Compatibilidade | O sistema é acessível em navegadores com HTML5. _(origem: rascunho de referência, RNF05)_ |
| RNF-03 | Segurança | As senhas do estudante, do administrador e do avaliador são guardadas de forma protegida (nunca em texto puro), e todo o acervo só é acessível a quem fez login. |
| RNF-04 | Desempenho | A pesquisa responde em até 3 segundos. _(valor de referência, a confirmar)_ |
| RNF-05 | Disponibilidade | Meta da versão em produção: o sistema fica disponível em horário comercial (referência: dias úteis, das 8h às 18h). Fora da entrega de 23/11/2026, que roda só em computador local para demonstração. |

## 10. Regras de negócio
| ID | Regra |
|---|---|
| RN-01 | O login do estudante é feito por matrícula e senha; a senha é definida pelo próprio estudante no primeiro acesso. |
| RN-02 | As matrículas válidas são cadastradas manualmente pelo administrador. |
| RN-03 | O login do administrador é independente do login por matrícula. |
| RN-04 | Quem envia o TCC ao repertório é o próprio estudante autenticado. |
| RN-05 | O avaliador (banca e mentores) tem um tipo de login próprio, diferente do de estudante e do de administrador. |
| RN-06 | Estudantes autenticados também podem pesquisar e baixar TCCs. |
| RN-07 | Banca e mentores são um único perfil (avaliador), com o mesmo acesso, pois o mentor de um semestre pode integrar a banca em outro. |
| RN-08 | Os avaliadores são cadastrados pelo administrador; não há autocadastro. |
| RN-09 | Todo TCC deve ter ao menos a monografia (PDF) e o arquivo de autoria; as demais partes são opcionais. |
| RN-10 | Um TCC só é aceito se tiver curso, ano, semestre, turma, nome do orientador, título e tecnologias/frameworks preenchidos, além da monografia (PDF) e do arquivo de autoria; isso evita TCCs sem identificadores e TCCs vazios. |
| RN-11 | O estudante edita o próprio TCC, mas não o exclui; o administrador exclui qualquer TCC, mas não edita. |
| RN-12 | O download é feito por parte do TCC, nunca do TCC completo de uma vez. |
| RN-13 | Cada arquivo enviado tem no máximo 50 MB. |
| RN-14 | Todo usuário logado (estudante, avaliador e administrador) vê e baixa todas as partes de todos os TCCs; não há visibilidade por arquivo. |
| RN-15 | A ordem padrão da lista de TCCs é do mais recente para o mais antigo, por ano e semestre; o título não define a posição na lista. |
| RN-16 | Uma única coordenação administra o repertório de todos os cursos de TI; o administrador não é restrito a um curso. |
| RN-17 | O estudante que esquece a senha pede a redefinição à coordenação; não há recuperação automática por e-mail. |
| RN-18 | O avaliador entra com um nome de usuário criado pela coordenação no cadastro e define a própria senha no primeiro acesso. |
| RN-19 | Há várias contas de administrador (membros da coordenação), criadas pela equipe de desenvolvimento antes da entrega; o sistema não cadastra administradores. |

## 11. Integrações
- **MongoDB (existente)**: o sistema envia para ele as informações do TCC (curso, ano, semestre, turma, orientador, título) e também os arquivos das partes (monografia, autoria, executável, código-fonte, slides, disclaimer). _(organização atual do banco existente: a confirmar antes da modelagem)_
- Sistema da faculdade: sem integração técnica no MVP. As matrículas são originárias dele, mas cadastradas manualmente (ver Fora do escopo).

## 12. Restrições
- Prazo: entrega do MVP em **23/11/2026**.
- Equipe de 10 pessoas; apenas 1 tem experiência com MongoDB e a experiência da equipe em desenvolvimento web não foi levantada.
- Formato de TCC/MVP.
- Arquivos de até 50 MB, guardados no MongoDB (decisão confirmada, sem Object Storage): como o limite de um documento comum é 16 MB, arquivos maiores exigem o mecanismo próprio de arquivos grandes do MongoDB (GridFS).

## 13. Critérios de aceite gerais
_(proposta, a validar com o orientador)_
- Todos os requisitos Must atendem aos seus critérios de aceite.
- OBJ-03 e OBJ-04: nenhum TCC enviado pelo repertório fica sem os campos e arquivos obrigatórios.
- OBJ-01, OBJ-02 e OBJ-05 demonstráveis ao orientador: achar um TCC pela pesquisa, baixar só uma parte e ver os mais recentes no topo da lista.
- O MVP é entregue e aprovado pelo professor orientador até 23/11/2026.

## 14. Glossário
| Termo | Definição |
|---|---|
| Repertório | Acervo web de TCCs dos cursos de TI. |
| TCC | Trabalho de Conclusão de Curso; composto por vários itens (monografia, executável, código-fonte, slides, disclaimer, autoria). |
| Monografia | Documento em PDF do TCC; único item obrigatório. |
| Hierarquia de identificação | Curso > ano > semestre > turma; é a forma atual de organizar os TCCs. |
| Banca | Avaliadores do TCC, que precisam localizar trabalhos pelo acervo. Pertence ao perfil avaliador. |
| Mentor | Professor que orienta TCCs e consulta o acervo. Pertence ao perfil avaliador. |
| Parte do TCC | Cada arquivo que compõe um TCC: monografia, autoria, executável, código-fonte, apresentação, disclaimer. |
| Autoria | Arquivo anexado pelo estudante no envio do TCC (parte obrigatória). |
| Avaliador | Perfil de acesso único que reúne banca e mentores. |
| Matrícula | Identificador do estudante no sistema da faculdade, usado como credencial de login. |

---
**Status da fase**: [ ] Em andamento  [ ] Aguardando aprovação  [x] Aprovado em: 16/10/2026
