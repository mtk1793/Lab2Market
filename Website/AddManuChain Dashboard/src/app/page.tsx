'use client'

// Dashboard for AddManuChain - v2
import { useState } from 'react'
import {
  Sidebar,
  Header,
  OverviewPage,
  OnboardingTutorial,
  useOnboarding,
  OrdersPage,
  BlueprintsPage,
  CentersPage,
  AnalyticsPage,
  SettingsPage,
  AuditLogPage,
  PartnersPage,
  ShipmentsPage,
  MaterialsPage,
  CertificationsPage,
  AuthoritiesPage,
  CustomerSuccessPage,
  DigitalInventoryPage,
  PrintApprovalPage,
  PhysicalInventoryPage,
} from '@/components/dashboard'

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview')
  const [mobileOpen, setMobileOpen] = useState(false)
  const { showOnboarding, isLoading, completeOnboarding } = useOnboarding()

  const getPageTitle = () => {
    switch (activeTab) {
      case 'overview':
        return { title: 'Dashboard Overview', subtitle: 'Welcome back, John' }
      case 'orders':
        return { title: 'Orders', subtitle: 'Manage and track your part orders' }
      case 'print_queue':
        return { title: 'Print Queue', subtitle: 'DRM approval pipeline — OEM & Certification Authority sign-offs' }
      case 'physical_inventory':
        return { title: 'Physical Inventory', subtitle: 'Manage physical spare parts across all sites' }
      case 'digital_inventory':
        return { title: 'Digital Inventory', subtitle: 'AI-driven parts forecasting and onsite readiness' }
      case 'blueprints':
        return { title: 'Blueprint Library', subtitle: 'Manage certified CAD blueprints' }
      case 'centers':
        return { title: 'Print Centers', subtitle: 'Monitor certified AM facilities' }
      case 'shipments':
        return { title: 'Shipments', subtitle: 'Track delivery logistics' }
      case 'materials':
        return { title: 'Materials Inventory', subtitle: 'Raw material stock management' }
      case 'partners':
        return { title: 'OEM Partners', subtitle: 'Manage partner relationships' }
      case 'analytics':
        return { title: 'Analytics', subtitle: 'Performance insights and reports' }
      case 'audit':
        return { title: 'Audit Logs', subtitle: 'System activity and compliance tracking' }
      case 'certifications':
        return { title: 'Certifications', subtitle: 'Compliance and certification management' }
      case 'authorities':
        return { title: 'Certification Authorities', subtitle: 'Manage relationships with certifying bodies' }
      case 'services':
        return { title: 'Customer Success', subtitle: 'End-to-end service and training management' }
      case 'settings':
        return { title: 'Settings', subtitle: 'Manage your account preferences' }
      default:
        return { title: 'Dashboard', subtitle: '' }
    }
  }

  const renderPage = () => {
    switch (activeTab) {
      case 'overview':
        return <OverviewPage />
      case 'orders':
        return <OrdersPage />
      case 'print_queue':
        return <PrintApprovalPage />
      case 'physical_inventory':
        return <PhysicalInventoryPage />
      case 'digital_inventory':
        return <DigitalInventoryPage />
      case 'blueprints':
        return <BlueprintsPage />
      case 'centers':
        return <CentersPage />
      case 'shipments':
        return <ShipmentsPage />
      case 'materials':
        return <MaterialsPage />
      case 'partners':
        return <PartnersPage />
      case 'analytics':
        return <AnalyticsPage />
      case 'audit':
        return <AuditLogPage />
      case 'certifications':
        return <CertificationsPage />
      case 'authorities':
        return <AuthoritiesPage />
      case 'services':
        return <CustomerSuccessPage />
      case 'settings':
        return <SettingsPage />
      default:
        return <OverviewPage />
    }
  }

  const pageInfo = getPageTitle()

  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      {/* Onboarding Tutorial for first-time users */}
      {!isLoading && showOnboarding && (
        <OnboardingTutorial onComplete={completeOnboarding} />
      )}

      {/* Sidebar (mobile controlled) */}
      <Sidebar
        activeTab={activeTab}
        onTabChange={(t) => { setActiveTab(t); setMobileOpen(false); }}
        mobileOpen={mobileOpen}
        onMobileClose={() => setMobileOpen(false)}
      />

      {/* Main Content */}
      <div className="ml-0 md:ml-64 transition-all duration-300">
        {/* Header */}
        <Header
          title={pageInfo.title}
          subtitle={pageInfo.subtitle}
          onNavigate={setActiveTab}
          mobileOpen={mobileOpen}
          setMobileOpen={setMobileOpen}
        />

        {/* Page Content */}
        <main className="min-h-[calc(100vh-64px)]">{renderPage()}</main>
      </div>
    </div>
  )
}
