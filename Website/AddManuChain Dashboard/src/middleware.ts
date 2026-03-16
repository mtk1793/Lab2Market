import { withAuth } from 'next-auth/middleware'

export default withAuth(
  function middleware() {
    return undefined
  },
  {
    callbacks: {
      authorized: ({ token }) => !!token,
    },
  }
)

export const config = {
  matcher: [
    '/((?!api/auth|api/contact|_next/static|_next/image|favicon|icon|manifest|apple-touch-icon|login).*)',
  ],
}
