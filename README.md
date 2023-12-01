# Data-Engineering-Golovata

## Prepare the project
- Clone the repo locally
  ```
  git clone https://github.com/robot-dreams-code/Data-Engineering-Golovata.git
  ```
  or You can get the link by clicking the `Code` button in the repo.
- Open the project folder in your IDE
- Open a terminal in the project folder
- Create a branch for the solution and switch on it
  ```
  git checkout -b your_name/lessonNN
  ```
- If there is 'requirements.txt` in lessonNN folder install the required packages:
  ```
  pip install -r requirements.txt
  ```

## Implement the solution…
- commit changes locally when done (can repeat as many times as needed)
  ```
  git commit -am "My changes description"
  ```
- Push the solution to the repo
  ```
  git push 
  ```
  if the branch doesn't exist on origin (`no upstream branch` error) yet you need to create it from the local copy instead (only need to do it once for a branch):
  ```
  git push --set-upstream origin your_name/lessonNN
  ```

## Create a Pull Request (PR)
- Open your repo on GitHub and create a `Pull Request` (PR): `Pull requests` tab -> `New pull request`.
- Select your branch in the dropdown (`base` should be `main` and `compare` is your `your_name/lessonNN` branch).
- Verify the PR details and code (scroll down to see it) and confirm (`Create pull request` button). Add meaningful title and description, click `Create pull request` button.
- PR is updated automatically after a push to your branch on GitHub server.
- After updating your PR - click on re-request button at PR page IF YOU NEED ADDITIONAL REVIEW OF YOUR CODE.