from datetime import datetime
from sqlalchemy import Date, DateTime, Integer, String, ForeignKey, Float
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from dio_fastapi_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    data_nascimento: Mapped[Date] = mapped_column(Date, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    data_cadastro: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atletas", lazy='selectin') # type: ignore
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates="atleta", lazy='selectin') # type: ignore
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_de_treinamento.pk_id"))
