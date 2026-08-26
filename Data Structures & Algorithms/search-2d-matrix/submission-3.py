class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        row = []
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                break
            elif matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][-1] > target:
                r = mid - 1

        if not row:
            return False

        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2

            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            elif row[mid] == target:
                return True

        return False


            