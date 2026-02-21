'use client'

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'
import { Separator } from '@/components/ui/separator'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { User, Building, Bell, Shield, CreditCard, Globe } from 'lucide-react'

export function SettingsPage() {
  return (
    <div className="p-6 space-y-6 max-w-4xl">
      {/* Profile Settings */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-[#0EA5E9]/10 flex items-center justify-center">
              <User className="w-5 h-5 text-[#0EA5E9]" />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Profile Settings</CardTitle>
              <CardDescription>Manage your personal information</CardDescription>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="firstName">First Name</Label>
              <Input id="firstName" defaultValue="John" className="bg-white border-slate-200" />
            </div>
            <div className="space-y-2">
              <Label htmlFor="lastName">Last Name</Label>
              <Input id="lastName" defaultValue="Operator" className="bg-white border-slate-200" />
            </div>
          </div>
          <div className="space-y-2">
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              defaultValue="j.operator@horizonmaritime.com"
              className="bg-white border-slate-200"
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="role">Role</Label>
            <Input id="role" defaultValue="Supply Chain Manager" className="bg-white border-slate-200" />
          </div>
          <Button className="bg-[#0EA5E9] hover:bg-[#0EA5E9]/90 text-white">Save Changes</Button>
        </CardContent>
      </Card>

      {/* Organization Settings */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-[#14B8A6]/10 flex items-center justify-center">
              <Building className="w-5 h-5 text-[#14B8A6]" />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Organization</CardTitle>
              <CardDescription>Your company information and preferences</CardDescription>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="companyName">Company Name</Label>
              <Input
                id="companyName"
                defaultValue="Horizon Maritime"
                className="bg-white border-slate-200"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="sector">Sector</Label>
              <Select defaultValue="offshore">
                <SelectTrigger className="bg-white border-slate-200">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="offshore">Offshore Oil & Gas</SelectItem>
                  <SelectItem value="naval">Naval & Defense</SelectItem>
                  <SelectItem value="arctic">Arctic & Remote Utilities</SelectItem>
                  <SelectItem value="other">Other</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
          <div className="space-y-2">
            <Label htmlFor="location">Primary Location</Label>
            <Input
              id="location"
              defaultValue="St. John's, NL, Canada"
              className="bg-white border-slate-200"
            />
          </div>
          <div className="space-y-2">
            <Label htmlFor="timezone">Timezone</Label>
            <Select defaultValue="america_st_johns">
              <SelectTrigger className="bg-white border-slate-200">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="america_st_johns">America/St. John's (NST)</SelectItem>
                <SelectItem value="america_halifax">America/Halifax (AST)</SelectItem>
                <SelectItem value="america_toronto">America/Toronto (EST)</SelectItem>
                <SelectItem value="america_vancouver">America/Vancouver (PST)</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </CardContent>
      </Card>

      {/* Notification Settings */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-[#F59E0B]/10 flex items-center justify-center">
              <Bell className="w-5 h-5 text-[#F59E0B]" />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Notifications</CardTitle>
              <CardDescription>Configure how you receive updates</CardDescription>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Order Status Updates</p>
              <p className="text-sm text-slate-500">Get notified when order status changes</p>
            </div>
            <Switch defaultChecked />
          </div>
          <Separator />
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Print Completion Alerts</p>
              <p className="text-sm text-slate-500">Notify when a print job is complete</p>
            </div>
            <Switch defaultChecked />
          </div>
          <Separator />
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Quality Check Results</p>
              <p className="text-sm text-slate-500">Alerts for quality inspection outcomes</p>
            </div>
            <Switch defaultChecked />
          </div>
          <Separator />
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Weekly Reports</p>
              <p className="text-sm text-slate-500">Receive weekly performance summaries</p>
            </div>
            <Switch />
          </div>
          <Separator />
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Email Notifications</p>
              <p className="text-sm text-slate-500">Also send notifications via email</p>
            </div>
            <Switch defaultChecked />
          </div>
        </CardContent>
      </Card>

      {/* Security Settings */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-[#0F172A]/5 flex items-center justify-center">
              <Shield className="w-5 h-5 text-[#0F172A]" />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">Security</CardTitle>
              <CardDescription>Account security and access control</CardDescription>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
            <div>
              <p className="font-medium text-[#0F172A]">Two-Factor Authentication</p>
              <p className="text-sm text-slate-500">Add an extra layer of security</p>
            </div>
            <Button variant="outline">Enable 2FA</Button>
          </div>
          <div className="space-y-2">
            <Label htmlFor="currentPassword">Change Password</Label>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
              <Input
                id="currentPassword"
                type="password"
                placeholder="Current password"
                className="bg-white border-slate-200"
              />
              <Input
                type="password"
                placeholder="New password"
                className="bg-white border-slate-200"
              />
              <Button variant="outline">Update Password</Button>
            </div>
          </div>
          <Separator />
          <div>
            <p className="font-medium text-[#0F172A] mb-2">Active Sessions</p>
            <div className="space-y-2">
              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                <div>
                  <p className="text-sm text-[#0F172A]">Chrome on Windows</p>
                  <p className="text-xs text-slate-500">St. John's, NL • Current session</p>
                </div>
                <Badge className="bg-[#14B8A6]/10 text-[#14B8A6]">Active</Badge>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* API Access */}
      <Card className="bg-white border-slate-200">
        <CardHeader>
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-[#6366F1]/10 flex items-center justify-center">
              <Globe className="w-5 h-5 text-[#6366F1]" />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold text-[#0F172A]">API Access</CardTitle>
              <CardDescription>Integration settings for external systems</CardDescription>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label>API Key</Label>
            <div className="flex gap-2">
              <Input
                type="password"
                value="amc_live_****************************"
                readOnly
                className="bg-slate-50 border-slate-200"
              />
              <Button variant="outline">Copy</Button>
              <Button variant="outline">Regenerate</Button>
            </div>
            <p className="text-xs text-slate-500">
              Use this key to integrate AddManuChain with your internal systems
            </p>
          </div>
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium text-[#0F172A]">Webhook URL</p>
              <p className="text-sm text-slate-500">Receive real-time order updates</p>
            </div>
            <Button variant="outline">Configure</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

// Badge component for settings page
function Badge({ className, children }: { className?: string; children: React.ReactNode }) {
  return (
    <span className={`px-2 py-1 text-xs font-medium rounded-full ${className}`}>
      {children}
    </span>
  )
}
