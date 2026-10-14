
"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import logging
import secrets
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

ORDERS = {
    "T1": {
        "guest": "Liam",
        "items": 3,
        "bill": 45.0,
        "is_settled": False,
    },
    "T2": {
        "guest": "Sophia",
        "items": 1,
        "bill": 18.0,
        "is_settled": True,
    },
    "T3": {
        "guest": "Mason",
        "items": 4,
        "bill": 72.0,
        "is_settled": False,
    },
}


def place_table_order(
    table_id: str,
    guest: str,
    items_count: int,
    order_log: Optional[list[str]] = None,
) -> bool:
    """Create a table order and optionally log the operation."""
    if not table_id.strip() or not guest.strip():
        raise ValueError("Table ID and guest name must not be empty.")

    if not isinstance(items_count, int) or isinstance(items_count, bool):
        raise TypeError("Item count must be an integer.")

    if items_count <= 0:
        raise ValueError("Item count must be greater than zero.")

    if table_id in ORDERS:
        return False

    ORDERS[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }

    if order_log is not None:
        order_log.append(
            f"Created order for {table_id} with {items_count} dishes"
        )

    return True


def void_table_order(table_id: str) -> bool:
    """Remove an order if it exists."""
    return ORDERS.pop(table_id, None) is not None


def check_table_status(table_id: str) -> bool:
    """Return True if an existing order is still unsettled."""
    order = ORDERS.get(table_id)
    return order is not None and not order["is_settled"]


def calculate_discounted_bill(
    table_id: str,
    discount_rate: float = 0.10,
) -> float:
    """Calculate the bill after applying a valid discount."""
    if table_id not in ORDERS:
        raise KeyError(f"No order found for table {table_id!r}.")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be numeric.")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_bill = ORDERS[table_id]["bill"]
    return round(base_bill * (1 - discount_rate), 2)


def generate_ticket_hash(table_id: str) -> str:
    """Generate a SHA-256 hash for a table ticket."""
    return hashlib.sha256(table_id.encode("utf-8")).hexdigest()


def generate_pos_pin() -> str:
    """Generate a secure, four-digit POS PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_kitchen_orders(
    filename: str = "kitchen_orders.txt",
) -> None:
    """Export active orders to a text file."""
    output_path = Path(filename)
    output_path.write_text(
        f"{ORDERS}\n",
        encoding="utf-8",
    )
    logging.info("Kitchen orders exported to %s", output_path)


def get_pending_summary(orders_to_check: dict) -> int:
    """Count orders that have not been settled."""
    return sum(
        not details["is_settled"]
        for details in orders_to_check.values()
    )


def main() -> None:
    """Execute sample restaurant billing operations."""
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print("Discounted Bill:", calculate_discounted_bill("T1"))
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())

    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(ORDERS))


if __name__ == "__main__":
    main()
