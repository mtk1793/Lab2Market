# AddManuChain User Guide
**Digital Inventory Platform for Offshore Oil & Gas**

Version 1.0 | February 2026

---

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [User Roles & Permissions](#user-roles--permissions)
3. [Dashboard Overview](#dashboard-overview)
4. [Core Features](#core-features)
5. [Quick Start Guides by Role](#quick-start-guides-by-role)
6. [Troubleshooting](#troubleshooting)
7. [FAQs](#faqs)

---

## 🚀 Getting Started

### Accessing AddManuChain

1. **Navigate to:** `https://your-domain.com` (or `http://localhost:3000` for development)
2. **Login Page:** You'll be redirected to the login page if not authenticated
3. **Enter Credentials:** Use your email and password provided by your administrator

### Demo Accounts (Development Only)

| Role | Email | Password | Purpose |
|------|-------|----------|---------|
| **Platform Admin** | admin@almatech.com | admin123 | Full system access, manage all resources |
| **Operator** | operator@statoil.com | operator123 | Place orders, track shipments |
| **OEM Partner** | partner@oem.com | partner123 | Manage blueprints, view analytics |

⚠️ **Security Note:** Change these credentials before production deployment!

---

## 👥 User Roles & Permissions

### 1. **Platform Admin** 🔑
*Full system access - Alma-Tech internal team*

**Permissions:**
- ✅ Manage all users and roles
- ✅ Access all customer data
- ✅ Modify system settings
- ✅ View comprehensive analytics
- ✅ Manage certification authorities
- ✅ Oversee customer engagements
- ✅ Handle training sessions

**Use Cases:**
- System configuration
- Customer onboarding
- Analytics and reporting
- Quality assurance

---

### 2. **Customer Admin** 👔
*Operations manager at offshore facility*

**Permissions:**
- ✅ View company orders and blueprints
- ✅ Place new orders
- ✅ Manage team operators
- ✅ Access company analytics
- ✅ Communicate with support
- ❌ Cannot see other companies' data

**Use Cases:**
- Oversee remote operations
- Approve urgent part orders
- Track cost savings
- Team management

---

### 3. **Operator** 🔧
*Rig worker or technician*

**Permissions:**
- ✅ Browse blueprint library
- ✅ Place part orders
- ✅ Track order status
- ✅ Submit customization requests
- ❌ Cannot approve orders
- ❌ Limited analytics access

**Use Cases:**
- Emergency part ordering
- Track delivery status
- Report part failures
- Request design modifications

---

### 4. **OEM Partner** 🏭
*Blueprint IP owner*

**Permissions:**
- ✅ Upload blueprints
- ✅ Manage blueprint versions
- ✅ View print analytics
- ✅ Track revenue from prints
- ✅ Submit certification requests
- ❌ Cannot access customer data

**Use Cases:**
- License part designs
- Monitor usage
- Ensure certification compliance
- Revenue tracking

---

### 5. **Print Center** 🖨️
*Certified 3D printing facility*

**Permissions:**
- ✅ Receive print jobs
- ✅ Update job status
- ✅ Manage material inventory
- ✅ Report capacity
- ❌ Cannot create orders

**Use Cases:**
- Process print orders
- Update production status
- Manage material stocks
- Quality control

---

### 6. **Certification Authority** 🛡️
*Regulatory body (DNV, Lloyd's Register, etc.)*

**Permissions:**
- ✅ Review certification requests
- ✅ Approve/reject blueprints
- ✅ Track approved parts
- ✅ Manage certification records
- ❌ Cannot access financial data

**Use Cases:**
- Blueprint certification review
- Compliance verification
- Industry standards enforcement

---

## 📊 Dashboard Overview

### Navigation Sidebar

The left sidebar contains the main navigation:

📖 **Core Operations**
- **Overview** - Dashboard home with KPIs
- **Orders** - Part order management
- **Blueprints** - Digital part library

🏢 **Facilities & Network**
- **Print Centers** - Certified facilities network
- **Shipments** - Logistics tracking
- **Materials** - Raw material inventory

🤝 **Partners & Services**
- **OEM Partners** - Blueprint IP owners
- **Customer Success** - End-to-end service tracking
- **Certifications** - Compliance management

📈 **Insights & Reports**
- **Analytics** - Performance metrics & ROI
- **Authorities** - Certification body relationships
- **Audit Logs** - Activity tracking

⚙️ **System**
- **Settings** - Account preferences

---

## 🎯 Core Features

### 1. **Blueprint Library**

**Purpose:** Digital inventory of certified part designs

**Key Actions:**
- **Browse:** Filter by category, material, OEM, certification status
- **Search:** Find parts by name or ID
- **View Details:** CAD file, material specs, certification, print count
- **Upload** (OEM Partners only): Add new blueprint designs
- **Request Modification** (Operators): Suggest design changes

**Example Use Case:**
*An operator needs a valve body for an emergency repair:*
1. Navigate to Blueprints
2. Filter by category: "Valves"
3. Select certified part: "Actuator Valve Body - SS316L"
4. Click "Order Part" → Redirects to order creation

---

### 2. **Order Management**

**Purpose:** On-demand part ordering and tracking

**Order Workflow:**
```
Pending → Printing → Quality Check → Shipped → Delivered
```

**Key Actions:**
- **Create Order:** Select blueprint, quantity, priority, destination
- **Track Status:** Real-time updates on production progress
- **View ETA:** Estimated delivery time
- **History:** All past orders with audit trail

**Priority Levels:**
- 🔴 **High** - Critical failure, production halted
- 🟡 **Medium** - Needed soon, no immediate impact
- 🟢 **Low** - Preventive maintenance, stock replenishment

**Example Use Case:**
*Critical pump impeller failure on offshore rig:*
1. Navigate to Orders → "New Order"
2. Select blueprint: "Pump Impeller - 316SS"
3. Set priority: High
4. Add notes: "Critical - Pump down"
5. Submit → Automatically routed to nearest certified print center
6. Track progress via Shipments page

---

### 3. **Print Center Network**

**Purpose:** Monitor certified 3D printing facilities

**Key Information:**
- **Location:** Geographic distribution
- **Status:** Online, Busy, Offline
- **Capacity:** Available printers, current utilization
- **Certifications:** DNV, Lloyd's Register, ABS, etc.
- **Materials:** Supported materials (steels, alloys)
- **Specialties:** Expertise areas (marine, oil & gas, complex geometries)

**Example Use Case:**
*Check nearest print center for urgent order:*
1. Navigate to Print Centers
2. Filter by: "Online" + "Capacity > 50%"
3. View: "Halifax Marine AM Center" - 85% capacity, DNV certified
4. Contact: Direct email/phone available

---

### 4. **Shipment Tracking**

**Purpose:** Real-time logistics visibility

**Tracking Stages:**
```
Preparing → In Transit → Out for Delivery → Delivered
```

**Key Information:**
- **Tracking ID:** Unique shipment identifier
- **Carrier:** Logistics provider
- **Origin/Destination:** From print center to rig
- **Progress:** Visual progress bar
- **ETA:** Estimated arrival
- **Distance:** Total miles

**Alerts:**
- 🚨 **Delayed:** Behind schedule
- ⚠️ **Weather Hold:** Environmental delays
- ✅ **On Time:** Tracking as expected

---

### 5. **Certification Authorities**

**Purpose:** Manage relationships with regulatory bodies

**Key Information:**
- **Authority Directory:** DNV, Lloyd's Register, ABS, Bureau Veritas, ISO
- **Specializations:** Marine, offshore, oil & gas
- **Performance Metrics:**
  - Parts approved
  - Average lead time
  - Pending requests
- **Contact Information:** Direct liaison details

**Certification Request Workflow:**
```
Submitted → Under Review → Approved/Rejected
```

**Example Use Case:**
*Submit new blueprint for DNV certification:*
1. Navigate to Authorities
2. Select "DNV - Marine & Offshore"
3. Click "New Certification Request"
4. Upload blueprint + testing data
5. Submit → Tracks approval process
6. Receive notification when approved

---

### 6. **Customer Success**

**Purpose:** End-to-end service implementation tracking

**Implementation Phases:**
```
Assessment → Adoption → Integration → Training → Maintenance
```

**Tab 1: Customer Engagements**
- **Customer List:** All active implementations
- **Phase Tracking:** Current stage of implementation
- **Health Score:** 0-100 customer satisfaction
- **Rig Count:** Number of rigs using platform
- **Milestones:** Date tracking for each phase

**Tab 2: Training Sessions**
- **Onboarding:** Platform usage training
- **Safety:** AM-specific safety protocols
- **Maintenance:** Equipment care procedures
- **Advanced:** Design modification skills

**Example Use Case:**
*Track Shell's implementation progress:*
1. Navigate to Customer Success
2. View engagement: "Shell Offshore"
3. Current phase: "Integration" (78% complete)
4. Health score: 85/100
5. Next milestone: Training scheduled for March 15, 2026

---

### 7. **Analytics Dashboard**

**Purpose:** Data-driven insights and ROI validation

**Key Metrics:**

**A. Operational KPIs**
- Total orders (all-time)
- Active orders (in-progress)
- Delivered parts (completed)
- Average lead time (days)
- Cost savings (USD)

**B. Comparative Analytics** (Just-on-Time vs Just-in-Case)
- **Lead Time Reduction:** 81% improvement (21 days → 4 days)
- **Warehouse Savings:** 81% cost reduction ($450K → $85K annually)
- **Repair Rate:** 65% parts repaired vs 0% traditional
- **Design Flexibility:** 15 custom iterations vs 1-2 OEM
- **Environmental Impact:**
  - CO₂ saved (kg)
  - Transportation miles avoided
  - Waste reduction (kg)

**Visual Components:**
- Line charts: Lead time trends
- Bar charts: Cost comparison
- Progress bars: Capacity utilization
- Cards: Quick stat summaries

**Example Use Case:**
*Prepare quarterly business review for CFO:*
1. Navigate to Analytics
2. Export comparative metrics
3. Show: $365K annual savings, 81% lead time reduction
4. Environmental benefit: 1,247 kg CO₂ saved
5. Design flexibility: 47 custom modifications enabled

---

### 8. **Materials Inventory**

**Purpose:** Track raw material stocks across print centers

**Key Information:**
- **Material Type:** Carbon steel, stainless steel, specialty alloys
- **Total Stock:** Aggregated inventory (kg)
- **Stock Status:**
  - 🟢 **Adequate:** Above reorder point
  - 🟡 **Low:** Below reorder point
  - 🔴 **Critical:** Urgent replenishment needed
- **Distribution:** Stock by print center
- **Lead Time:** Supplier delivery time
- **Unit Cost:** Per kg pricing

**Example Use Case:**
*Check material availability before large order:*
1. Navigate to Materials
2. Search: "316 Stainless Steel"
3. Total stock: 2,450 kg (Adequate)
4. Distribution: Halifax (1,200 kg), St. John's (850 kg), Aberdeen (400 kg)
5. Sufficient for order: ✅

---

### 9. **Audit Logs**

**Purpose:** Compliance and activity tracking

**Logged Activities:**
- Order creation/status changes
- Blueprint uploads/modifications
- User actions (who did what, when)
- Certification approvals
- System configuration changes

**Key Information:**
- **Timestamp:** Precise date/time
- **User:** Who performed action
- **Action Type:** Created, Updated, Deleted, Approved, etc.
- **Details:** Specific changes made
- **Order ID:** Related order (if applicable)

**Example Use Case:**
*Investigate order delay for customer inquiry:*
1. Navigate to Audit Logs
2. Filter by Order ID: "ORD-2847"
3. View timeline:
   - Created: Feb 1, 2026 09:15 AM
   - Printing started: Feb 1, 2026 10:30 AM
   - Quality check: Feb 2, 2026 02:00 PM
   - Shipped: Feb 2, 2026 04:00 PM
   - Delivered: Feb 3, 2026 11:00 AM
4. Total time: 49 hours 45 minutes

---

## 🎓 Quick Start Guides by Role

### For Operators: "I Need a Part Urgently"

**Scenario:** A hydraulic valve has failed on your rig and production is halted.

**Steps:**
1. **Login** → operator@company.com
2. **Navigate** → Blueprints
3. **Search** → "hydraulic valve"
4. **Select** → "Hydraulic Control Valve - SS316L" (DNV certified)
5. **Click** → "Order Part"
6. **Fill Form:**
   - Quantity: 1
   - Priority: High
   - Notes: "Critical failure - production halted"
   - Destination: Pre-filled with your rig location
7. **Submit Order**
8. **Track** → Navigate to Orders → View status updates
9. **ETA** → 3-4 days (displayed on order page)
10. **Receive** → Get email notifications at each stage

**Expected Timeline:**
- Printing: 12-18 hours
- Quality check: 2-4 hours
- Shipping prep: 1-2 hours
- Transit: 2-3 days
- **Total: 3-4 days** (vs. 21 days traditional OEM)

---

### For OEM Partners: "I Want to License My Design"

**Scenario:** You're an OEM with certified valve designs you want to license to offshore operators.

**Steps:**
1. **Login** → partner@oem.com
2. **Navigate** → Blueprints
3. **Click** → "+ New Blueprint"
4. **Upload CAD File** → .STEP, .STL, or .SLDPRT
5. **Fill Details:**
   - Name: "Actuator Valve Body"
   - Category: Valves
   - Material: 316L Stainless Steel
   - Certification: DNV-GL (if already certified)
   - Status: Pending Review (if awaiting certification)
6. **Submit** → Alma-Tech team reviews (1-2 business days)
7. **Certification Request (if needed):**
   - Navigate to Authorities
   - Select certification body (e.g., DNV)
   - Submit request with test data
   - Track approval status
8. **Monitor Usage:**
   - Navigate to Analytics
   - View prints of your blueprints
   - Track revenue attribution

**Revenue Model:**
- Per-print licensing fee
- Revenue dashboard shows real-time earnings
- Monthly statements generated

---

### For Customer Admins: "I Need to Track Our ROI"

**Scenario:** Your CFO wants to know if AddManuChain is delivering cost savings.

**Steps:**
1. **Login** → admin@company.com
2. **Navigate** → Analytics
3. **View KPIs:**
   - Total orders: 47
   - Average lead time: 4.2 days (vs. 21 days traditional)
   - Cost savings: $128,450 (this quarter)
4. **Scroll to Comparative Analytics:**
   - Lead time reduction: 80%
   - Warehouse savings: $365,000/year
   - Design modifications enabled: 8 custom parts
   - Environmental impact: 342 kg CO₂ saved
5. **Export Data:**
   - Click "Export Report"
   - Generate PDF for stakeholder presentation
6. **Review Customer Success:**
   - Navigate to Customer Success (if available)
   - View implementation health score: 85/100
   - Upcoming training: March 15, 2026

**Business Case Summary:**
- **Cost Savings:** $365K/year warehouse reduction
- **Time Savings:** 81% faster delivery
- **Flexibility:** Custom designs impossible with traditional OEM
- **ESG Benefits:** Significant CO₂ reduction

---

### For Print Centers: "I Need to Update Job Status"

**Scenario:** You've completed printing a part and it's ready for quality check.

**Steps:**
1. **Login** → printcenter@facility.com
2. **Navigate** → Orders
3. **Filter** → Status: "Printing" + Assigned to: Your Center
4. **Select Order** → ORD-2847
5. **Update Status** → "Quality Check"
6. **Add Notes** → "Print completed successfully, moving to QC"
7. **Upload Photo** → Attach image of completed part
8. **Save** → Operator automatically notified
9. **Materials Management:**
   - Navigate to Materials
   - Update stock: Reduced by part weight
   - Check reorder point: If low, request replenishment

**Status Updates:**
- **Printing:** Job in progress
- **Quality Check:** Post-processing inspection
- **Shipped:** Handed to logistics
- **Delivered:** Confirmed receipt by customer

---

## 🛠️ Troubleshooting

### Login Issues

**Problem:** "Invalid email or password"
**Solution:**
1. Verify email is correct (check for typos)
2. Password is case-sensitive
3. Contact your admin to reset password
4. Check Caps Lock is off

**Problem:** "Unable to connect to server"
**Solution:**
1. Check internet connection
2. Verify URL is correct
3. Try clearing browser cache
4. Contact IT support if issue persists

---

### Order Issues

**Problem:** "Cannot find blueprint for my part"
**Solution:**
1. Check spelling in search
2. Try browsing by category instead
3. Contact OEM partner to request blueprint upload
4. Submit customization request for similar part

**Problem:** "Order status not updating"
**Solution:**
1. Refresh page (F5 or Ctrl+R)
2. Check last update timestamp
3. Contact print center directly
4. View audit logs for activity history

**Problem:** "ETA seems too long"
**Solution:**
1. Check order priority (Low = longer)
2. Verify print center capacity
3. Consider upgrading to High priority
4. Check for weather/logistics delays in Shipments

---

### Technical Issues

**Problem:** "Page won't load / slow performance"
**Solution:**
1. Check internet speed
2. Clear browser cache and cookies
3. Try different browser (Chrome, Firefox, Edge)
4. Disable browser extensions temporarily
5. Contact support: support@addmanuchain.com

**Problem:** "Upload failed" (for blueprints)
**Solution:**
1. Check file size (max 50MB)
2. Supported formats: .STEP, .STL, .SLDPRT, .IGES
3. Verify file isn't corrupted
4. Try compressing file if too large
5. Contact support for large files

---

## ❓ FAQs

### General

**Q: How long does a typical order take?**
**A:** 3-5 days average, compared to 21+ days for traditional OEM supply. High-priority orders can be expedited.

**Q: Are all parts certified?**
**A:** Yes, all blueprints in the library are certified by recognized classification societies (DNV, Lloyd's Register, ABS, etc.) for offshore use.

**Q: Can I request custom modifications?**
**A:** Absolutely! Navigate to Blueprints → Select part → "Request Customization". Our engineering team reviews within 48 hours.

**Q: What materials are available?**
**A:** Carbon steels, stainless steels (316L, 316, 304), PH martensitic stainless, specialty marine alloys. Check Materials page for current inventory.

---

### For Operators

**Q: What if I don't find the exact part I need?**
**A:** Submit a customization request with details about your application. Our team can modify existing designs or create new ones.

**Q: Can I order multiple quantities?**
**A:** Yes, specify quantity in order form. Bulk orders may have longer lead times depending on print center capacity.

**Q: How do I know my part will fit?**
**A:** All blueprints include detailed specifications. You can download CAD files to verify dimensions before ordering.

---

### For OEM Partners

**Q: How do I protect my intellectual property?**
**A:** All blueprints are encrypted and access-controlled. Only certified print centers and authorized users can view designs. Legal agreements protect IP rights.

**Q: How is revenue calculated?**
**A:** Per-print licensing fee based on negotiated agreement. View real-time earnings in Analytics → Partner Revenue.

**Q: What if someone modifies my design?**
**A:** All customizations require OEM approval. You maintain control over derivative works.

---

### For Customer Admins

**Q: How do I add new users to my company?**
**A:** Contact your Alma-Tech account manager to provision new users. Roles and permissions are assigned during setup.

**Q: Can I see costs breakdown?**
**A:** Yes, Analytics page shows detailed cost savings, warehouse reductions, and ROI calculations. Custom reports available on request.

**Q: How secure is our data?**
**A:** Enterprise-grade security: encrypted data in transit and at rest, role-based access control, audit logging, SOC 2 compliant (when available).

---

### Technical

**Q: Which browsers are supported?**
**A:** Chrome (recommended), Firefox, Safari, Edge. Latest two versions of each. IE not supported.

**Q: Is there a mobile app?**
**A:** Currently web-only, optimized for desktop. Mobile-responsive interface in development.

**Q: Can I integrate with our ERP system?**
**A:** API integration available for enterprise customers. Contact sales for details.

---

## 📞 Support Contacts

### Technical Support
- **Email:** support@addmanuchain.com
- **Phone:** +1 (902) 555-0123
- **Hours:** 24/7 for critical issues, 8 AM - 6 PM AST for general inquiries

### Account Management
- **Email:** accounts@addmanuchain.com
- **Phone:** +1 (902) 555-0124
- **Hours:** Monday-Friday, 9 AM - 5 PM AST

### Emergency (Production-Critical Issues)
- **Hotline:** +1 (902) 555-URGENT
- **Available:** 24/7/365

---

## 📚 Additional Resources

- **Video Tutorials:** [tutorials.addmanuchain.com](https://tutorials.addmanuchain.com)
- **API Documentation:** [docs.addmanuchain.com](https://docs.addmanuchain.com)
- **Blog & Updates:** [blog.addmanuchain.com](https://blog.addmanuchain.com)
- **Certification Standards:** [standards.addmanuchain.com](https://standards.addmanuchain.com)

---

**Document Version:** 1.0  
**Last Updated:** February 23, 2026  
**Next Review:** May 2026  

---

*For training sessions, contact your account manager or email training@addmanuchain.com*
