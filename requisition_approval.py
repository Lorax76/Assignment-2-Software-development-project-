from add_requisition import add_requisition

def requisition_approval(requisition):
    status = "Pending"
    total = requisition["total"]
    staff_id = requisition["staff_id"]
    req_id = requisition["req_id"]

    if total < 500:
        status = "Approved"
        approval_ref = staff_id + str(req_id)[-3:]
    else:
        approval_ref = "N/A"

    requisition["status"] = status
    requisition["approval_ref"] = approval_ref

    print("Total: $", total)
    print("Status:", status)
    print("Approval Reference Number:", approval_ref)


def display_requisitions(requisition):
    print("\nPrinting requisitions:")
    print("Date:", requisition["date"])
    print("Requisition ID:", requisition["req_id"])
    print("Staff ID:", requisition["staff_id"])
    print("Staff Name:", requisition["staff_name"])
    print("Total $", requisition["total"])
    print("Status:", requisition["status"])
    print("Approval Reference Number:", requisition["approval_ref"])


# Run all tasks
data = add_requisition()
requisition_approval(data)
display_requisitions(data)




