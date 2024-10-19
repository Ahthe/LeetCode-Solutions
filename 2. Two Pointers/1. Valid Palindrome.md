# 1. Valid Palindrome  (Easy)

Created: October 13, 2024 4:50 AM
Status: Easy
Updated: October 19, 2024 4:52 AM

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Example 1:**

```java
Input: s = "Was it a car or a cat I saw?"

Output: true
```

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**

```java
Input: s = "tab a cat"

Output: false
```

Explanation: "tabacat" is not a palindrome.

**Constraints:**

- `1 <= s.length <= 1000`
- `s` is made up of only printable ASCII characters.

## Solution

Time Complexity: O(n)  The time complexity of this solution is O(n), where n is the length of the input string 's'. In the worst case, we might need to traverse the entire string once to determine if it is a valid palindrome.

Space Complexity: O(1)  The space complexity is O(1) since we are not using any additional data structures that depend on the input size. We only use a constant amount of extra space for the two pointers and other variables.

```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		# Initializing two pointers, left and right
		l, r = 0, len(s) - 1
			
		# loop until the two pointers meet
		while l < r:
					
			# Move the left pointer to the right if its not alphaNum
			while l < r and not self.alphaNum(s[l])
				l += 1
					
			# Move the right pointer to the left if its not alphaNum
			while r > l and not self.alphaNum(s[r])
				r -= 1
					
			# Compare characters in lower case manner
			if s[l].lower() != s[r].lower()
				
				return False
					
			# Move both pointers towards the center
			l, r = l + 1, r - 1
			
		# If all characters matched, its a palindrome
		return True
			
	def alphaNum(self, char):
		return(
			ord('A') <= ord('char') <= ord('Z') or	
			ord('a') <= ord('char') <= ord('z') or
			ord('0') <= ord('char') <= ord('9')
	)
```

## Notes

- **Initializing pointers**:
    - "First, I'm initializing two pointers, `l` and `r`. The left pointer `l` starts at the beginning of the string, and the right pointer `r` starts at the end. These will help me check characters from both ends of the string towards the center."
- **Handling non-alphanumeric characters**:
    - "Next, I’ll enter a while loop to move both pointers towards the center. Before comparing characters, I need to skip over any non-alphanumeric characters. I'll use two inner while loops to move the left pointer forward and the right pointer backward until I find valid alphanumeric characters."
- **Checking for palindrome condition**:
    - "Once I've moved the pointers to valid characters, I’ll check if the characters are the same, ignoring case. If they don’t match, I know the string is not a palindrome and can return `False` immediately."
- **Updating pointers**:
    - "If the characters match, I’ll increment the left pointer and decrement the right pointer to continue checking the next pair of characters."
- **Return true after checking all characters**:
    - "If I make it through the entire string without finding mismatches, I can confidently return `True`, indicating that the string is a palindrome."
- **Helper function explanation**:
    - "The `alphaNum` helper function checks whether a character is alphanumeric by comparing its ASCII values. It returns `True` for any character between 'A' and 'Z', 'a' and 'z', or '0' and '9'. This allows me to properly skip over non-alphanumeric characters when processing the string."

## Example Walkthrough and Edge Cases

### Consider the string: `"A man, a plan, a canal: Panama"`

1. **Initialization**:
    - `l = 0` (points to `'A'`)
    - `r = 29` (points to `'a'`)
2. **Comparison**:
    - The characters at `l = 0` (`'A'`) and `r = 29` (`'a'`) are compared (case-insensitively). Since `'A' == 'a'`, the pointers move inward.
    - `l = 1`, `r = 28`
3. **Skip spaces**:
    - `l = 1` points to a space `' '`, so `l` moves to `2`.
    - Similarly, `r = 28` points to a space `'m'`, so `r` moves to `27`.
4. **Comparison**:
    - Now, `l = 2` points to `'m'` and `r = 27` points to `'m'`. They match, so the pointers move inward again.
    - `l = 3`, `r = 26`
5. **Repeat**:
    - This process continues, skipping non-alphanumeric characters and comparing the rest, until `l` crosses `r`. Since all characters matched, the method returns `True`.

### Edge Cases

- **Empty String**:
An empty string (`""`) is trivially a palindrome. The loop won't run, returning `True`.
- **Single Character**:
A single character string (e.g., `"a"`) is a palindrome by definition. The loop won't run, returning `True`.
- **Non-Alphanumeric Only**:
For strings like `"!!!"`, all characters are skipped, and the function returns `True`.
- **Case-Sensitivity**:
The comparison is case-insensitive due to `s[l].lower() != s[r].lower()`.
- **Non-Palindrome**:
For a non-palindrome like `"hello"`, the first mismatch returns `False`.

## Similar Questions