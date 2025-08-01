# Enunciado: Sistema de Gestão de Consultório Médico
# Objetivo:
# Desenvolver uma aplicação de consola em Python, utilizando os princípios da Programação Orientada por Objetos (POO), para simular a gestão de um consultório médico. A aplicação deve permitir o registo de médicos, pacientes, marcação de consultas e emissão de um relatório de agenda diária.
# Funcionalidades obrigatórias:
# Registar Médicos
# Nome, especialidade, número da cédula profissional.
# Registar Pacientes
# Nome, data de nascimento, número do cartão de cidadão.
# Marcar Consultas
# Associar um médico e um paciente a uma data e hora específica.
# Garantir que o médico não tem duas consultas marcadas ao mesmo tempo.
# Listagens
# Listar Consultas do Dia
# Mostrar todas as consultas agendadas para uma data específica, ordenadas por hora.
# Listar Médicos e Pacientes
# Listagens completas com todos os dados.
# Exportar para ficheiro as consultas para text

#Trabalho final - Jaynne Lino

from datetime import datetime

class Consultorio:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.consultas = []


    def registar_medico(self, medico):
        for med in self.medicos:
            if med._cedula == medico._cedula:
                raise ValueError("Já existe um médico com esta cédula.")
            if med._NIF == medico._NIF:
                raise ValueError("Nif já cadastrado.")
            if med._cartao_cidadao == medico._cartao_cidadao:
                raise ValueError("Cartão de Cidadão já cadastrado.")
        self.medicos.append(medico)
        

    def registar_paciente(self, paciente):
        for pt in self.pacientes:
            if pt._NIF == paciente._NIF:
                raise ValueError("NIF já cadastrado.")
            if pt._cartao_cidadao == paciente._cartao_cidadao:
                raise ValueError("Cartão de Cidadão já cadastrado.") 
        self.pacientes.append(paciente)
    
    def marcar_consulta(self, nova_consulta):
        for consulta in self.consultas:
            if consulta.medico == nova_consulta.medico and consulta.data_hora == nova_consulta.data_hora:
                raise ValueError(f"O médico {nova_consulta.medico.nome} já tem uma consulta marcada para {nova_consulta.data_hora}.")
            if consulta.paciente == nova_consulta.paciente and consulta.data_hora == nova_consulta.data_hora:
                raise ValueError(f"O paciente {nova_consulta.paciente.nome} já tem uma consulta marcada para {nova_consulta.data_hora}.")
        
        self.consultas.append(nova_consulta)

    def get_medico(self, cedula):
        for medico in self.medicos:
            if medico._cedula == cedula:
                return medico
        raise ValueError("Médico não encontrado.")
    
    def get_paciente(self, cartao_cidadao):
        for paciente in self.pacientes:
            if paciente._cartao_cidadao == cartao_cidadao:
                return paciente
        raise ValueError("Paciente não encontrado.")

    
    def listar_consultas(self):
        consultas_ordenadas = sorted(self.consultas, key=lambda c: c.data_hora)
        print(f"\n----------Total de consultas marcadas: {len(self.consultas)}----------\n")
        for consulta in consultas_ordenadas:
            print(f"Consulta: Dr. {consulta.medico.nome} com {consulta.paciente.nome} na data {consulta.data_hora}")

    def listar_consultas_do_dia(self):
        hoje = datetime.today()
        consultas_do_dia = [c for c in self.consultas if c.data_hora.date() == hoje]
        consultas_ordenadas = sorted(consultas_do_dia, key=lambda c: c.data_hora) 
        if not consultas_do_dia:
            print(f"\n----- Não há consultas marcadas para hoje ({hoje.strftime('%d/%m/%Y')}) -----\n")
            return  
        print(f"\n----- Consultas marcadas para hoje ({hoje.strftime('%d/%m/%Y')}): {len(consultas_do_dia)} -----\n")
        for consulta in consultas_ordenadas:
            print(f"Consulta: Dr. {consulta.medico.nome} com {consulta.paciente.nome} na data {consulta.data_hora.strftime('%d/%m/%Y %H:%M')}")
            
            
    def listar_consultas_intervalo(self, data_inicio, data_fim):
        try:
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d %H:%M")
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d %H:%M")
        except ValueError:
            print("\nErro: A data deve estar no formato 'YYYY-MM-DD HH:MM' (ex: 2025-01-01 08:30)")
            return 

        consultas_dia = []

        print("\n----------Consultas dentro intervalo escolhido:----------\n")

        for consulta in self.consultas:
            if data_inicio <= consulta.data_hora <= data_fim:
                consultas_dia.append(consulta)

        consultas_dia.sort(key=lambda c: c.data_hora)

        print(f"Consultas entre {data_inicio} e {data_fim}:")
        for consulta in consultas_dia:
            print(f"Consulta: Dr. {consulta.medico.nome} com {consulta.paciente.nome} na data {consulta.data_hora.strftime('%Y-%m-%d %H:%M')}")
        

    def listar_medicos(self):
        print("\n----------Lista de Médicos:----------\n")
        for medico in self.medicos:
            print(medico)

    def listar_pacientes(self):
        print("\n----------Lista de Pacientes:----------\n")
        for paciente in self.pacientes:
            print(paciente)

    def listar_todos_dados(self):
        print("\n----------Relatório Completo:----------\n")
        self.listar_medicos()
        self.listar_pacientes()
        self.listar_consultas()

    def exportar_txt(self, nome_arquivo="consultas.txt"):
        with open(nome_arquivo, "w", encoding="utf-8") as exportar:
            for consulta in consultorio.consultas:
                linha = (f"Consulta: Dr. {consulta.medico.nome} com {consulta.paciente.nome} "
                        f"na data {consulta.data_hora.strftime('%Y-%m-%d %H:%M')}\n")
                exportar.write(linha)
        print(f"\nConsultas exportadas para o ficheiro '{nome_arquivo}.txt'.\n")
    
                  
class Pessoa:
    def __init__(self, nome, data_nascimento, cartao_cidadao:str, NIF:str):
        self.nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
        self._cartao_cidadao = cartao_cidadao
        self._NIF = NIF
    

class Medico(Pessoa):
    def __init__(self, nome, especialidade, cedula, NIF, data_nascimento, cartao_cidadao):
        super().__init__(nome, data_nascimento, cartao_cidadao, NIF)
        self.especialidade = especialidade
        self._cedula = cedula
        
    def __str__(self):
        return f"Dr. {self.nome}, Especialidade: {self.especialidade}, Cédula: {self._cedula}, NIF: {self._NIF}, Data de Nascimento: {self._data_nascimento.strftime('%Y-%m-%d')}, Cartão de Cidadão: {self._cartao_cidadao}"

class Paciente(Pessoa):
    def __init__(self, nome, data_nascimento, cartao_cidadao, NIF):
        super().__init__(nome, data_nascimento, cartao_cidadao, NIF)
    def __str__(self):
        return f"Paciente: {self.nome}, Data de Nascimento: {self._data_nascimento.strftime('%Y-%m-%d')}, Cartão de Cidadão: {self._cartao_cidadao}, NIF: {self._NIF}"

class Consulta:
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M")
        


if __name__ == "__main__":



    print("Bem-vindo ao sistema de gestão de consultório médico!")
    consultorio = Consultorio()

    ##DADOS INICIAIS PARA TESTE

    medico1 = Medico("Silva", "Cardiologia", "12", "123456789", "1980-01-01", "CC123456")
    consultorio.registar_medico(medico1)
    paciente1 = Paciente("João", "2000-02-02", "CC1", "1")
    consultorio.registar_paciente(paciente1)
    consulta1 = Consulta(medico1, paciente1, "2025-10-01 10:00")
    consultorio.marcar_consulta(consulta1)
    medico2 = Medico("Costa", "Pediatria", "345", "987654321", "1985-05-05", "CC654321")
    consultorio.registar_medico(medico2)
    paciente2 = Paciente("Maria", "1995-03-03", "CC12", "2")
    consultorio.registar_paciente(paciente2)
    consulta2 = Consulta(medico2, paciente2, "2025-10-01 12:00")
    consultorio.marcar_consulta(consulta2)
    medico3 = Medico("Santos", "Dermatologia", "56", "456789123", "1990-10-10", "CC789123")
    consultorio.registar_medico(medico3)
    paciente3 = Paciente("Ana", "1990-04-04", "CC123", "3")
    consultorio.registar_paciente(paciente3)
    consulta3 = Consulta(medico1, paciente3, "2025-10-01 11:10")
    consultorio.marcar_consulta(consulta3)

    while True:
        print("\nMenu:")
        print("1. Registar Médico")
        print("2. Registar Paciente")
        print("3. Marcar Consulta")
        print("4. Listar Consultas")
        print("5. Listar Consultas do Dia")
        print("6. Listar consultas por Intervalo")
        print("7. Listar Médicos")
        print("8. Listar Pacientes")
        print("9. Relatório completo")
        print("0. Exportar consultas para Ficheiro")
        print("X. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\nRegistar Médico (ou digite 0 para voltar ao menu):")
            nome = input("Nome do médico: ")
            if nome == "0":
                continue
            especialidade = input("Especialidade: ")
            cedula = input("Número da cédula profissional: ")
            NIF = input("NIF: ")
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            cartao_cidadao = input("Número do cartão de cidadão: ")

            medico = Medico(nome, especialidade, cedula, NIF, data_nascimento, cartao_cidadao)
            try:
                consultorio.registar_medico(medico)
                print(f"Médico {medico.nome} registado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
    
            input("Pressione Enter para continuar")

        elif opcao == "2":
            print("\nRegistar Paciente (ou digite 0 para voltar ao menu):")
            nome = input("Nome do paciente: ")
            if nome == "0":
                continue
            data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            cartao_cidadao = input("Número do cartão de cidadão: ")
            NIF = input("NIF: ")

            paciente = Paciente(nome, data_nascimento, cartao_cidadao, NIF)

            try:
                consultorio.registar_paciente(paciente)
                print(f"\nPaciente {paciente.nome} registado com sucesso!\n")
            except ValueError as e:
                print(f"Erro: {e}")

            input("Pressione Enter para continuar")

        elif opcao == "3":
            print("\nMarcar Consulta:")
            medico_cedula = input("Número da cédula do médico: ")
            paciente_cartao = input("Número do cartão de cidadão do paciente: ")
            while True:
                data_hora = input("Data e hora da consulta (YYYY-MM-DD HH:MM): ")
                try:
                    medico = consultorio.get_medico(medico_cedula)
                    paciente = consultorio.get_paciente(paciente_cartao)
                    consulta = Consulta(medico, paciente, data_hora)
                    consultorio.marcar_consulta(consulta)
                    print(f"Consulta agendada com sucesso para o utente {paciente.nome} com o Dr. {medico.nome} na data {data_hora}.")
                    break
                except ValueError as e:
                    print(f"Erro ao marcar consulta: {e} Tente outra data/hora.")
            input("Pressione Enter para continuar")

        elif opcao == "4":
            print("\nListar todas as consultas:")
            consultorio.listar_consultas()
            input("Pressione Enter para continuar")
        
        elif opcao == "5":
            print("\nListar Consultas do dia:")
            consultorio.listar_consultas_do_dia()
            input("Pressione Enter para continuar")

        elif opcao == "6":
            print("\nListar Consultas por Intervalo:")
            data_inicio = input("Data e hora de início (YYYY-MM-DD HH:MM): ")
            data_fim = input("Data e hora de fim (YYYY-MM-DD HH:MM): ")
            consultorio.listar_consultas_intervalo(data_inicio, data_fim)
            input("Pressione Enter para continuar")
        
        elif opcao == "7":
            print("\nListar Médicos:")
            consultorio.listar_medicos()
            input("Pressione Enter para continuar")
        
        elif opcao == "8":
            print("\nListar Pacientes:")
            consultorio.listar_pacientes()
            input("Pressione Enter para continuar")

        elif opcao == "9":
            print("\nRelatório completo:")
            consultorio.listar_todos_dados()
            input("Pressione Enter para continuar")

        elif opcao == "0":
            print("\nExportar consultas para Ficheiro:")
            nome_arquivo = input("Nome do ficheiro: ")
            consultorio.exportar_txt(nome_arquivo)
            input("Pressione Enter para continuar")

        elif opcao.upper() == "X":
            print("Saindo do sistema. Até logo!")
            break



