from tkinter import *
from modules.helpers import customers
import os

def show_customer_list_window(root):
    customer_window = Toplevel(root)
    customer_window.title("Customer List")
    customer_window.geometry("625x500")

    # Keep references to images to prevent garbage collection
    image_refs = []

    # Scrollable canvas setup
    canvas = Canvas(customer_window)
    scrollbar = Scrollbar(customer_window, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    for customer in customers:
        frame = Frame(scrollable_frame, borderwidth=2, relief="solid", padx=10, pady=5)
        frame.pack(fill=X, pady=8, padx=8)

        # Load image if it exists, else use a placeholder
        img_path = customer.img
        if os.path.exists(img_path):
            try:
                if customer.name == "Carl Bundy":
                    photo = PhotoImage(file=img_path)  # Do not subsample for Carl Bundy
                else:
                    photo = PhotoImage(file=img_path).subsample(5, 5)  # Make others 2x smaller
            except Exception:
                photo = None
        else:
            photo = None

        if photo:
            img_label = Label(frame, image=photo)
            img_label.image = photo  # Keep reference
            img_label.grid(row=0, column=0, rowspan=5, sticky="nw", padx=(0,10), pady=2)
            image_refs.append(photo)
        else:
            # If image not found, just leave space
            img_label = Label(frame, width=64, height=64)
            img_label.grid(row=0, column=0, rowspan=5, sticky="nw", padx=(0,10), pady=2)

        # Customer info
        name_label = Label(frame, text=customer.name, font=("Arial", 12, "bold"))
        name_label.grid(row=0, column=1, sticky="w")

        area_label = Label(frame, text=f"Area: {customer.area}", font=("Arial", 10))
        area_label.grid(row=1, column=1, sticky="w")

        standards_label = Label(frame, text=f"Standards: {customer.standards}", font=("Arial", 10))
        standards_label.grid(row=2, column=1, sticky="w")

        affinity = customer.product_affinity
        affinity_label = Label(
            frame,
            text=f"Product Affinity: Weed: {affinity.weed:.2f}, Meth: {affinity.meth:.2f}, Cocaine: {affinity.cocaine:.2f} (Prefers: {affinity.get_highest_affinity().capitalize()})",
            font=("Arial", 10)
        )
        affinity_label.grid(row=3, column=1, sticky="w")

        spend_label = Label(frame, text=f"Spend Range: ${customer.min_spend} - ${customer.max_spend}", font=("Arial", 10))
        spend_label.grid(row=4, column=1, sticky="w")
