import { PrismaClient } from '@prisma/client'
import bcrypt from 'bcryptjs'

const prisma = new PrismaClient()

async function testLogin() {
  console.log('Testing user authentication...\n')
  
  const testAccounts = [
    { email: 'admin@almatech.com', password: 'admin123' },
    { email: 'operator@statoil.com', password: 'operator123' },
    { email: 'partner@oem.com', password: 'partner123' },
  ]
  
  for (const account of testAccounts) {
    console.log(`\n--- Testing: ${account.email} ---`)
    
    // Find user
    const user = await prisma.user.findUnique({
      where: { email: account.email }
    })
    
    if (!user) {
      console.log(`❌ User not found in database`)
      continue
    }
    
    console.log(`✅ User found: ${user.name}`)
    console.log(`   Role: ${user.role}`)
    console.log(`   Company: ${user.company}`)
    console.log(`   Has password: ${user.password ? 'Yes' : 'No'}`)
    
    if (user.password) {
      const isValid = await bcrypt.compare(account.password, user.password)
      console.log(`   Password valid: ${isValid ? '✅ YES' : '❌ NO'}`)
    }
  }
  
  console.log('\n\n--- All Users in Database ---')
  const allUsers = await prisma.user.findMany({
    select: {
      email: true,
      name: true,
      role: true,
      password: true,
    }
  })
  
  console.log(`Total users: ${allUsers.length}`)
  allUsers.forEach(user => {
    console.log(`  - ${user.email} (${user.role}) - Password: ${user.password ? 'Set' : 'NOT SET'}`)
  })
}

testLogin()
  .then(() => {
    console.log('\n✅ Test complete')
    process.exit(0)
  })
  .catch((error) => {
    console.error('❌ Error:', error)
    process.exit(1)
  })
