export async function api(path: string, opts: RequestInit = {}) {
  const res = await fetch(`http://localhost:8000${path}`, opts)
  if (!res.ok) throw new Error('erro api')
  return res.json()
}
