# מד הדלק השבועי

A one-file weekly budget tracker (Hebrew, RTL). Open `index.html`, or serve it with GitHub Pages.

- Weekly limit with a fuel-gauge; the low-fuel lamp blinks under 20% left.
- Overspending in a week is deducted from the next week's limit.
- Monthly verdict: met the monthly budget → trophy + amount saved; missed → rain cloud + amount over.
- Data lives in the browser's localStorage. With Firebase configured, it also syncs between everyone who joined the same shared household.

## Shared sync (Firebase)

1. Create a project at https://console.firebase.google.com (Analytics not needed).
2. **Build → Authentication → Get started → Sign-in method → Anonymous → Enable.**
   Under **Settings → Authorized domains**, add `adichoUNI.github.io`.
3. **Build → Firestore Database → Create database** (production mode, any region), then paste `firestore.rules` into the **Rules** tab and publish.
4. **Project settings → Your apps → Web (`</>`)**, register an app, and copy the `firebaseConfig` object into `FIREBASE_CONFIG` at the top of the script in `index.html`.
5. In the app: ⚙️ → **יצירת חשבון משותף** → **שליחת קישור הזמנה**. Opening the invite link on another device joins it. Expenses already recorded on each device are uploaded on its first connection.

The Firebase config is not secret (it identifies the project); access is controlled by the rules and the household code, which is in the invite link — share it only with whoever should see the budget.
