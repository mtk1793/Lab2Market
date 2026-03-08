// Authentication API route disabled
// import NextAuth from 'next-auth'
// import { authOptions } from '@/lib/auth'

// const handler = NextAuth(authOptions)

// export { handler as GET, handler as POST }

// Return empty responses since authentication is disabled
export async function GET() {
  return new Response('Authentication disabled', { status: 404 })
}

export async function POST() {
  return new Response('Authentication disabled', { status: 404 })
}
