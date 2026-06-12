"""Alternative Version des Merge-Sort-Skripts auf dem main-Branch."""

from __future__ import annotations

from collections.abc import Sequence

import matplotlib.pyplot as plt


def merge(left_values: list[int], right_values: list[int]) -> list[int]:
    """Führe zwei bereits sortirte Listen zu einer sortierten Liste zusammen"""
    merged_values: list[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] <= right_values[right_index]:
            merged_values.append(left_values[left_index])
            left_index += 1
        else:
            merged_values.append(right_values[right_index])
            right_index += 1

    # Falls in einer Hälfte noch Werte übrig sind, werden sie angehängt.
    merged_values.extend(left_values[left_index:])
    merged_values.extend(right_values[right_index:])

    return merged_values


def merge_sort(values: Sequence[int]) -> list[int]:
    """Sortiere Werte mit Merge-Sort-Algorithmus und gib eine neue Liste zurück"""
    values = list(values)

    if len(values) <= 1:
        return values

    middle_index = len(values) // 2
    left_half = merge_sort(values[:middle_index])
    right_half = merge_sort(values[middle_index:])

    return merge(left_half, right_half)


def plot_sorting_result(original_values: Sequence[int], sorted_values: Sequence[int]) -> None:
    """Vergleiche die Werte vor und nach dem Sortieren in einem Diagramm."""
    indices = range(len(original_values))

    plt.figure(figsize=(9, 5))
    plt.plot(indices, original_values, marker="o", label="Vor dem Sortieren")
    plt.plot(indices, sorted_values, marker="o", label="Nach dem Sortieren")

    plt.title("Vergleich der Werte vor und nach Merge Sort")
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Führe ein Beispiel aus und visualisiere die Werte vor und nch dem Sortieren"""
    original_values = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_values = merge_sort(original_values)

    print(f"Ursprüngliche Werte: {original_values}")
    print(f"Sortierte Werte:     {sorted_values}")

   # plot_values(original_values, "Werte vor dem Sortieren")
   # plot_values(sorted_values, "Werte nach Merge Sort")

   plot_sorting_result(original_values, sorted_values)


if __name__ == "__main__":
    main()