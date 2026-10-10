from datetime import datetime
from typing import List, Optional


class Usuario:

  def __init__(
      self, id: int, nome: str, matricula: str, email: str, tipo_perfil: str
  ) -> None:
    pass

  def autenticar(self) -> bool:
    pass


class Aluno(Usuario):

  def __init__(
      self,
      id: int,
      nome: str,
      matricula: str,
      email: str,
      tipo_perfil: str,
      curso: str,
  ) -> None:
    pass

  def submeter_tcc(self, dados_tcc: dict, arquivos: List["Arquivo"]) -> "TCC":
    pass

  def atualizar_tcc(self, tcc_id: int, dados_tcc: dict) -> bool:
    pass


class Professor(Usuario):

  def __init__(
      self,
      id: int,
      nome: str,
      matricula: str,
      email: str,
      tipo_perfil: str,
      departamento: str,
  ) -> None:
    pass

  def orientar_tcc(self, tcc_id: int) -> bool:
    pass

  def avaliar_tcc(self, tcc_id: int, status: str, parecer: str) -> bool:
    pass


class Administrador(Usuario):

  def __init__(
      self, id: int, nome: str, matricula: str, email: str, tipo_perfil: str
  ) -> None:
    pass

  def moderar_sistema(self, entidade: str, entidade_id: int) -> bool:
    pass

  def gerenciar_usuarios(
      self, acao: str, usuario_id: Optional[int] = None
  ) -> bool:
    pass


class TCC:

  def __init__(
      self,
      id: int,
      titulo: str,
      resumo: str,
      ano: int,
      tecnologias: str,
      status_aprovacao: str,
      link_repositorio_git: Optional[str] = None,
  ) -> None:
    pass

  def cadastrar(self) -> bool:
    pass

  def editar(self, novos_dados: dict) -> bool:
    pass

  def deletar(self) -> bool:
    pass

  @staticmethod
  def pesquisar(termo: str, filtros: dict) -> List["TCC"]:
    pass


class Arquivo:

  def __init__(
      self,
      id: int,
      nome_arquivo: str,
      caminho_armazenamento: str,
      tipo_arquivo: str,
      tamanho_bytes: int,
  ) -> None:
    pass

  def baixar(self) -> bytes:
    pass


class Compilacao:

  def __init__(
      self,
      id: int,
      status_compilacao: str,
      log_saida: str,
      data_execucao: datetime,
  ) -> None:
    pass

  def executar_sandbox(self, arquivo_id: int) -> dict:
    pass


class Notificacao:

  def __init__(
      self,
      id: int,
      mensagem: str,
      tipo: str,
      lido: bool,
      data_envio: datetime,
  ) -> None:
    pass

  def enviar(self, usuario_id: int) -> bool:
    pass