import java.util.Arrays;

public class Test{
  public static void main(String[] args) {
   int[] arr = {8, 5, 3, 7, 7, 2};
   System.out.println(Arrays.toString(bubble_sort(arr)));

   int target = 1;
   System.out.println(binary_search(target, arr));

   tryingSomeFitchesFromAnotherLanguage();
  }

  public static int[] bubble_sort(int[] arr) {
    if (arr.length <= 1){
      return arr;
    }

    boolean swapped = true;
    while (swapped == true) {

      swapped = false;      

      for ( int i = 0; i < arr.length - 1; i++) {

        if (arr[i] > arr[i + 1]) {
          int temp = arr[i];
          arr[i] = arr[i + 1];
          arr[i + 1] = temp;

          swapped = true;
        }
      }
    }
    return arr;
  }


  public static boolean binary_search (int target, int[] arr) {
    arr = bubble_sort(arr);

    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
      int mid = (left + right ) / 2;
      int expected = arr[mid];

      if (expected == target) {
        return true;
      } else if (expected < target){
        right = mid - 1;
      } else{
        left = mid + 1;
      }
    }
    return false;   
  }

  public static void tryingSomeFitchesFromAnotherLanguage() {
    int[] arr1 = {1, 2, 3, 4};
    int[] arr2 = {1, 2, 3, 4};
    // arr1.equals(arr2) - просто сравнивает ссылки, поэтому выводит false
    System.out.println(arr1.equals(arr2));
    // Arrays.equals(arr1, arr2) - сравнивает значение массивов, поэтому выводит true
    System.out.println(Arrays.equals(arr1, arr2));
    
  }
}
