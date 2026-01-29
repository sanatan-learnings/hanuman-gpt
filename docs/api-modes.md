# API Modes Comparison

The Hanuman Chalisa spiritual guidance feature supports two modes for OpenAI API access.

## Mode 1: User-Provided API Key (Current)

**How it works:**
- Users enter their own OpenAI API key
- Key stored in browser localStorage
- Direct API calls from browser to OpenAI

**Pros:**
✅ No backend needed
✅ No ongoing costs for you
✅ Simple setup

**Cons:**
❌ Users need their own OpenAI account
❌ More friction (API key entry)
❌ Users see their key in browser

**Configuration:**
```javascript
// assets/js/guidance.js
const WORKER_URL = ''; // Empty = user-provided key mode
```

---

## Mode 2: Cloudflare Worker (Recommended)

**How it works:**
- Your API key stored securely in Cloudflare
- Users make requests to your worker
- Worker proxies to OpenAI

**Pros:**
✅ No API key needed from users
✅ Key hidden from users
✅ Frictionless experience
✅ Keep GitHub Pages hosting
✅ Rate limiting built-in
✅ Free tier (100k requests/day)

**Cons:**
❌ 10 minutes initial setup
❌ You pay for all OpenAI usage

**Configuration:**
```javascript
// assets/js/guidance.js
const WORKER_URL = 'https://hanuman-chalisa-api.your-subdomain.workers.dev';
```

---

## Switching Between Modes

### Enable Worker Mode
1. Deploy Cloudflare Worker (see [cloudflare-worker-setup.md](cloudflare-worker-setup.md))
2. Update `WORKER_URL` in `assets/js/guidance.js` with your worker URL
3. Commit and push

### Disable Worker Mode (Revert to User API Key)
1. Set `WORKER_URL = ''` in `assets/js/guidance.js`
2. Commit and push

That's it! No other code changes needed.

---

## Cost Comparison

### Mode 1: User-Provided Key
- **You pay:** $0 (users pay their own OpenAI costs)
- **User pays:** ~$0.01 per query

### Mode 2: Cloudflare Worker
- **You pay:**
  - Cloudflare: $0 (free tier: 100k requests/day)
  - OpenAI: ~$0.01 per user query
- **User pays:** $0

**Example:** 100 queries/day = $1/day = $30/month OpenAI costs

---

## Which Should I Choose?

### Choose User-Provided Key if:
- You want zero ongoing costs
- Your users are technical (comfortable with API keys)
- Low traffic site
- Testing/development

### Choose Cloudflare Worker if:
- You want best user experience
- Users shouldn't need OpenAI accounts
- You can afford $0.01 per query
- Production site
- Want analytics and rate limiting

---

## Hybrid Approach (Future)

Possible to support both modes simultaneously:
- Check if `WORKER_URL` is set
- If yes, use worker (no API key UI)
- If no, show API key input

Current implementation already supports this! Just change `WORKER_URL`.

---

## Security Notes

### Mode 1 (User Key)
- Key stored in browser localStorage
- Visible in browser DevTools
- Each user controls their own key

### Mode 2 (Worker)
- Your key stored as Cloudflare secret
- Never exposed to browser
- You control rate limiting and access
- **Recommendation:** Set CORS to your domain only

---

## Questions?

See [cloudflare-worker-setup.md](cloudflare-worker-setup.md) for deployment guide.
