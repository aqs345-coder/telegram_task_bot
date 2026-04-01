from database.connection import init_db
from services import task_service

def _send_whatsapp_message(to_phone: str, message: str):
    """Simula o envio de uma mensagem via WhatsApp."""
    print(f"\n--- ENVIANDO MENSAGEM VIA WHATSAPP PARA {to_phone} ---")
    print(message)
    print("--------------------------------------------------")

def run_tests():
    # 1. Inicializa o banco (cria o arquivo sqlite e as tabelas)
    init_db()
    print("Banco de dados inicializado!\n")

    user_numero = "5511999999999"

    # 2. Testando CREATE
    print("Adicionando tarefas...")
    task_service.create_task(user_numero, "Estudar cálculo", "Estudos")
    task_service.create_task(user_numero, "Revisar código Python", "Trabalho")
    task_service.create_task(user_numero, "Comprar pão", "Casa")


    # 3. Testando READ
    print("\nListando pendências:")
    pendentes = task_service.get_pending_tasks(user_numero)
    for t in pendentes:
        print(f"[{t.id}] {t.title} ({t.category})")

    # 4. Testando UPDATE
    if pendentes:
        id_para_concluir = pendentes[0].id
        print(f"\nConcluindo a tarefa ID {id_para_concluir}...")
        task_service.complete_task(id_para_concluir, user_numero)

    # 5. Lendo novamente para confirmar
    print("\nListando pendências após conclusão:")
    pendentes_atualizadas = task_service.get_pending_tasks(user_numero)
    for t in pendentes_atualizadas:
        print(f"[{t.id}] {t.title} ({t.category})")

    # 6. Enviando status das tarefas via WhatsApp
    print("\nPreparando mensagem para WhatsApp...")
    all_tasks = task_service.get_all_tasks_for_user(user_numero)
    
    if all_tasks:
        message_lines = ["Olá! Aqui estão suas tarefas e seus status:"]
        for t in all_tasks:
            status = "Concluída" if t.is_completed else "Pendente"
            message_lines.append(f"[{t.id}] {t.title} ({t.category}) - {status}")
        
        whatsapp_message = "\n".join(message_lines)
        _send_whatsapp_message(user_numero, whatsapp_message)
    else:
        _send_whatsapp_message(user_numero, "Olá! Você não tem tarefas cadastradas.")


if __name__ == "__main__":
    run_tests()
