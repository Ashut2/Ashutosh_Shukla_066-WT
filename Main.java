public class Main {

    // Find the second largest element in the array without sorting.
    // Returns null if there is no second largest (e.g., all elements equal or array length < 2).
    public static Integer secondLargest(int[] arr) {
        if (arr == null || arr.length < 2) return null;

        Integer first = null;  // largest
        Integer second = null; // second largest (distinct)

        for (int num : arr) {
            if (first == null || num > first) {
                // new largest found, demote previous largest to second
                second = first;
                first = num;
            } else if (num != first && (second == null || num > second)) {
                // num is a candidate for second largest (distinct from largest)
                second = num;
            }
        }
        return second;
    }

    public static void main(String[] args) {
        int[] arr = {3, 5, 1, 4, 5};
        Integer second = secondLargest(arr);

        if (second != null) {
            System.out.println("Second largest: " + second);
        } else {
            System.out.println("No second largest (need at least two distinct elements)." );
        }

        // Example edge cases
        int[] allSame = {2, 2, 2};
        System.out.println("All same -> " + secondLargest(allSame)); // prints: All same -> null

        int[] small = {10};
        System.out.println("Single element -> " + secondLargest(small)); // prints: Single element -> null
    }
}
