'use client'

import { useState, useCallback } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTitle,
    DialogDescription,
    DialogFooter,
} from '@/components/ui/dialog'
import {
    KeyRound,
    ShieldCheck,
    ShieldAlert,
    CheckCircle2,
    Clock,
    Lock,
    Unlock,
    Building2,
    Award,
    Package,
    Zap,
    AlertTriangle,
    Eye,
} from 'lucide-react'
import { toast } from 'sonner'
import { orders as initialOrders, blueprints, printCenters, Order } from '@/lib/static-data'

// Approval pipeline steps
const PIPELINE_STEPS = [
    { id: 'submitted', label: 'Request Submitted', icon: Package, description: 'Customer submitted a print request' },
    { id: 'oem', label: 'OEM Approved', icon: Building2, description: 'OEM grants IP license for blueprint' },
    { id: 'cert', label: 'Cert Verified', icon: Award, description: 'Certification authority clears print center' },
    { id: 'token', label: 'Print Token Issued', icon: KeyRound, description: 'Secure one-time decryption key issued' },
]

function getPipelineStep(order: Order): number {
    if (order.printAuthToken) return 4
    if (order.certApproval.approved && order.oemApproval.approved) return 2
    if (order.certApproval.approved || order.oemApproval.approved) return 1
    return 0
}

function ApprovalStepper({ order }: { order: Order }) {
    const step = getPipelineStep(order)
    return (
        <div className="flex items-center gap-0 w-full">
            {PIPELINE_STEPS.map((s, idx) => {
                const Icon = s.icon
                const done = idx < step || (idx === 3 && order.printAuthToken)
                const active = idx === step && idx < 3
                return (
                    <div key={s.id} className="flex items-center flex-1 last:flex-none">
                        <div className="flex flex-col items-center gap-1">
                            <div className={`w-8 h-8 rounded-full flex items-center justify-center transition-all duration-500 ${done ? 'bg-emerald-500 text-white shadow-lg shadow-emerald-200' :
                                    active ? 'bg-[#0EA5E9] text-white animate-pulse' :
                                        'bg-slate-200 text-slate-400'
                                }`}>
                                {done ? <CheckCircle2 className="w-4 h-4" /> : <Icon className="w-4 h-4" />}
                            </div>
                            <span className={`text-[10px] font-medium text-center w-16 leading-tight ${done ? 'text-emerald-600' : active ? 'text-[#0EA5E9]' : 'text-slate-400'
                                }`}>{s.label}</span>
                        </div>
                        {idx < 3 && (
                            <div className={`flex-1 h-0.5 mx-1 transition-all duration-500 ${idx < step ? 'bg-emerald-400' : 'bg-slate-200'
                                }`} />
                        )}
                    </div>
                )
            })}
        </div>
    )
}

interface ApprovalCardProps {
    order: Order
    type: 'oem' | 'cert'
    onApprove: (orderId: string, type: 'oem' | 'cert') => void
}

function ApprovalCard({ order, type, onApprove }: ApprovalCardProps) {
    const blueprint = blueprints.find(b => b.id === order.blueprintId)
    const center = printCenters.find(c => c.id === order.centerId)
    const approval = type === 'oem' ? order.oemApproval : order.certApproval

    const certMatch = center && blueprint && center.certification === blueprint.certification
    const canApprove = type === 'cert' ? certMatch !== false : true

    return (
        <Card className={`border-2 transition-all duration-300 ${approval.approved
                ? 'border-emerald-200 bg-emerald-50/50'
                : 'border-slate-200 bg-white hover:border-[#0EA5E9]/30 hover:shadow-md'
            }`}>
            <CardContent className="p-4">
                <div className="flex items-start justify-between gap-3 mb-3">
                    <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                            <span className="font-mono text-sm font-bold text-[#0EA5E9]">{order.orderId}</span>
                            <Badge className={
                                order.priority === 'high' ? 'bg-red-100 text-red-600 text-xs' :
                                    order.priority === 'medium' ? 'bg-amber-100 text-amber-600 text-xs' :
                                        'bg-slate-100 text-slate-500 text-xs'
                            }>
                                {order.priority}
                            </Badge>
                        </div>
                        <p className="font-semibold text-[#0F172A] text-sm">{order.partName}</p>
                        <p className="text-xs text-slate-500 mt-0.5">Qty: {order.quantity} · {new Date(order.createdAt).toLocaleDateString()}</p>
                    </div>
                    <div className={`w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 ${approval.approved ? 'bg-emerald-500' : 'bg-slate-100'
                        }`}>
                        {approval.approved
                            ? <ShieldCheck className="w-5 h-5 text-white" />
                            : <Lock className="w-5 h-5 text-slate-400" />
                        }
                    </div>
                </div>

                {/* Blueprint & Center info */}
                <div className="space-y-1.5 mb-3">
                    {blueprint && (
                        <div className="flex items-center gap-2 text-xs text-slate-600 bg-slate-50 px-3 py-1.5 rounded-lg">
                            <KeyRound className="w-3 h-3 text-[#0EA5E9]" />
                            <span className="font-medium">{blueprint.blueprintId}</span>
                            <span className="text-slate-400">·</span>
                            <span>{blueprint.name}</span>
                            {type === 'oem' && (
                                <Badge className="ml-auto bg-purple-100 text-purple-700 text-[10px]">{blueprint.oem}</Badge>
                            )}
                        </div>
                    )}
                    {center && (
                        <div className={`flex items-center gap-2 text-xs px-3 py-1.5 rounded-lg ${type === 'cert'
                                ? certMatch
                                    ? 'bg-emerald-50 text-emerald-700'
                                    : 'bg-red-50 text-red-600'
                                : 'bg-slate-50 text-slate-600'
                            }`}>
                            <Building2 className="w-3 h-3" />
                            <span className="font-medium">{center.name}</span>
                            <span className="text-slate-400">·</span>
                            <span>{center.certification}</span>
                            {type === 'cert' && (
                                <Badge className={`ml-auto text-[10px] ${certMatch ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-600'
                                    }`}>
                                    {certMatch ? '✓ Match' : '✗ Mismatch'}
                                </Badge>
                            )}
                        </div>
                    )}
                </div>

                {/* Other approval status */}
                <div className="flex items-center gap-2 text-xs text-slate-500 mb-3">
                    {type === 'cert' ? (
                        <>
                            <Building2 className="w-3 h-3" />
                            <span>OEM:</span>
                            {order.oemApproval.approved
                                ? <span className="text-emerald-600 font-medium">✓ {order.oemApproval.approvedBy?.split('(')[0].trim()}</span>
                                : <span className="text-amber-500 font-medium">⏳ Awaiting OEM</span>
                            }
                        </>
                    ) : (
                        <>
                            <Award className="w-3 h-3" />
                            <span>Cert Auth:</span>
                            {order.certApproval.approved
                                ? <span className="text-emerald-600 font-medium">✓ {order.certApproval.approvedBy?.split('(')[0].trim()}</span>
                                : <span className="text-amber-500 font-medium">⏳ Awaiting</span>
                            }
                        </>
                    )}
                </div>

                {/* Action */}
                {approval.approved ? (
                    <div className="flex items-center gap-2 text-xs text-emerald-700 bg-emerald-50 px-3 py-2 rounded-lg">
                        <CheckCircle2 className="w-3.5 h-3.5" />
                        <span>Approved by <strong>{approval.approvedBy}</strong></span>
                    </div>
                ) : (
                    <Button
                        onClick={() => onApprove(order.id, type)}
                        disabled={!canApprove}
                        className={`w-full text-sm ${canApprove
                                ? type === 'oem'
                                    ? 'bg-purple-600 hover:bg-purple-700 text-white'
                                    : 'bg-emerald-600 hover:bg-emerald-700 text-white'
                                : 'bg-slate-100 text-slate-400 cursor-not-allowed'
                            }`}
                    >
                        {!canApprove ? (
                            <><AlertTriangle className="w-4 h-4 mr-2" />Cert Mismatch — Cannot Approve</>
                        ) : type === 'oem' ? (
                            <><Building2 className="w-4 h-4 mr-2" />Grant IP License</>
                        ) : (
                            <><Award className="w-4 h-4 mr-2" />Authorize Print Center</>
                        )}
                    </Button>
                )}
            </CardContent>
        </Card>
    )
}

export function PrintApprovalPage() {
    const [orders, setOrders] = useState(initialOrders)
    const [viewOrder, setViewOrder] = useState<Order | null>(null)
    const [approvingOrder, setApprovingOrder] = useState<{ id: string; type: 'oem' | 'cert' } | null>(null)
    const [isConfirmOpen, setIsConfirmOpen] = useState(false)

    const pendingOEM = orders.filter(o => !o.oemApproval.approved && !['delivered'].includes(o.status))
    const pendingCert = orders.filter(o => !o.certApproval.approved && !['delivered'].includes(o.status))
    const readyToPrint = orders.filter(o => o.oemApproval.approved && o.certApproval.approved && !o.printAuthToken && !['printing', 'quality_check', 'shipped', 'delivered'].includes(o.status))

    const handleApproveClick = (orderId: string, type: 'oem' | 'cert') => {
        setApprovingOrder({ id: orderId, type })
        setIsConfirmOpen(true)
    }

    const handleConfirmApproval = () => {
        if (!approvingOrder) return
        const { id, type } = approvingOrder
        const now = new Date().toISOString()

        setOrders(prev => prev.map(o => {
            if (o.id !== id) return o
            if (type === 'oem') {
                return { ...o, oemApproval: { approved: true, approvedAt: now, approvedBy: 'OEM Partner (Baker Hughes)' } }
            } else {
                return { ...o, certApproval: { approved: true, approvedAt: now, approvedBy: "Cert Authority (Lloyd's Register)" } }
            }
        }))

        const order = orders.find(o => o.id === id)
        if (type === 'oem') {
            toast.success(`IP License granted for ${order?.orderId}`, { description: 'OEM approval recorded in audit log.' })
        } else {
            toast.success(`Print Center authorized for ${order?.orderId}`, { description: 'Certification check passed. Recorded in audit log.' })
        }

        setIsConfirmOpen(false)
        setApprovingOrder(null)
    }

    const approvingOrderData = approvingOrder ? orders.find(o => o.id === approvingOrder.id) : null

    return (
        <div className="p-6 space-y-6">
            {/* Header Stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <Card className="bg-gradient-to-br from-purple-600 to-purple-700 border-none text-white">
                    <CardContent className="p-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="text-purple-200 text-xs font-medium">OEM Pending</p>
                                <p className="text-3xl font-bold">{pendingOEM.length}</p>
                            </div>
                            <Building2 className="w-8 h-8 text-purple-300" />
                        </div>
                    </CardContent>
                </Card>
                <Card className="bg-gradient-to-br from-emerald-600 to-emerald-700 border-none text-white">
                    <CardContent className="p-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="text-emerald-200 text-xs font-medium">Cert Pending</p>
                                <p className="text-3xl font-bold">{pendingCert.length}</p>
                            </div>
                            <Award className="w-8 h-8 text-emerald-300" />
                        </div>
                    </CardContent>
                </Card>
                <Card className="bg-gradient-to-br from-[#0EA5E9] to-[#14B8A6] border-none text-white">
                    <CardContent className="p-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="text-sky-200 text-xs font-medium">Ready to Print</p>
                                <p className="text-3xl font-bold">{readyToPrint.length}</p>
                            </div>
                            <Zap className="w-8 h-8 text-sky-200" />
                        </div>
                    </CardContent>
                </Card>
                <Card className="bg-gradient-to-br from-slate-700 to-slate-800 border-none text-white">
                    <CardContent className="p-4">
                        <div className="flex items-center justify-between">
                            <div>
                                <p className="text-slate-300 text-xs font-medium">Tokens Issued</p>
                                <p className="text-3xl font-bold">{orders.filter(o => o.printAuthToken).length}</p>
                            </div>
                            <KeyRound className="w-8 h-8 text-slate-400" />
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* Ready to Print Alert */}
            {readyToPrint.length > 0 && (
                <div className="flex items-center gap-3 p-4 bg-gradient-to-r from-[#0EA5E9]/10 to-[#14B8A6]/10 border border-[#0EA5E9]/30 rounded-xl">
                    <div className="w-10 h-10 rounded-full bg-[#0EA5E9] flex items-center justify-center flex-shrink-0">
                        <Zap className="w-5 h-5 text-white" />
                    </div>
                    <div className="flex-1">
                        <p className="font-semibold text-[#0F172A] text-sm">
                            {readyToPrint.length} order{readyToPrint.length > 1 ? 's' : ''} cleared for Secure Print
                        </p>
                        <p className="text-xs text-slate-500">All digital signatures obtained. Navigate to Orders to issue print tokens.</p>
                    </div>
                    <div className="flex items-center gap-1">
                        {readyToPrint.map(o => (
                            <Badge key={o.id} className="bg-[#0EA5E9] text-white text-xs">{o.orderId}</Badge>
                        ))}
                    </div>
                </div>
            )}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
                {/* OEM Approval Queue */}
                <div className="space-y-4">
                    <div className="flex items-center gap-3">
                        <div className="w-9 h-9 rounded-xl bg-purple-100 flex items-center justify-center">
                            <Building2 className="w-5 h-5 text-purple-600" />
                        </div>
                        <div>
                            <h2 className="font-bold text-[#0F172A]">OEM IP License Approvals</h2>
                            <p className="text-xs text-slate-500">Grant intellectual property rights per blueprint</p>
                        </div>
                        <Badge className="ml-auto bg-purple-100 text-purple-700">{pendingOEM.length} pending</Badge>
                    </div>
                    <div className="space-y-3 max-h-[600px] overflow-y-auto pr-1">
                        {pendingOEM.length === 0 ? (
                            <div className="text-center py-12 text-slate-400">
                                <ShieldCheck className="w-12 h-12 mx-auto mb-3 text-emerald-400" />
                                <p className="font-medium">All OEM approvals cleared</p>
                            </div>
                        ) : (
                            pendingOEM.map(order => (
                                <ApprovalCard key={order.id} order={order} type="oem" onApprove={handleApproveClick} />
                            ))
                        )}
                    </div>
                </div>

                {/* Cert Authority Queue */}
                <div className="space-y-4">
                    <div className="flex items-center gap-3">
                        <div className="w-9 h-9 rounded-xl bg-emerald-100 flex items-center justify-center">
                            <Award className="w-5 h-5 text-emerald-600" />
                        </div>
                        <div>
                            <h2 className="font-bold text-[#0F172A]">Certification Authority Approvals</h2>
                            <p className="text-xs text-slate-500">Verify print center holds valid certification for material</p>
                        </div>
                        <Badge className="ml-auto bg-emerald-100 text-emerald-700">{pendingCert.length} pending</Badge>
                    </div>
                    <div className="space-y-3 max-h-[600px] overflow-y-auto pr-1">
                        {pendingCert.length === 0 ? (
                            <div className="text-center py-12 text-slate-400">
                                <ShieldCheck className="w-12 h-12 mx-auto mb-3 text-emerald-400" />
                                <p className="font-medium">All cert authority approvals cleared</p>
                            </div>
                        ) : (
                            pendingCert.map(order => (
                                <ApprovalCard key={order.id} order={order} type="cert" onApprove={handleApproveClick} />
                            ))
                        )}
                    </div>
                </div>
            </div>

            {/* Pipeline Overview */}
            <Card className="bg-white border-slate-200">
                <CardHeader className="pb-3">
                    <CardTitle className="text-base font-semibold text-[#0F172A] flex items-center gap-2">
                        <ShieldCheck className="w-5 h-5 text-[#0EA5E9]" />
                        DRM Approval Pipeline — All Active Orders
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    <div className="space-y-4">
                        {orders.filter(o => !['delivered'].includes(o.status)).map(order => {
                            const blueprint = blueprints.find(b => b.id === order.blueprintId)
                            return (
                                <div key={order.id} className="p-4 bg-slate-50 rounded-xl">
                                    <div className="flex items-center justify-between mb-3">
                                        <div className="flex items-center gap-2">
                                            <span className="font-mono text-sm font-bold text-[#0EA5E9]">{order.orderId}</span>
                                            <span className="text-sm text-slate-600">{order.partName}</span>
                                            {blueprint && <Badge className="bg-slate-100 text-slate-600 text-[10px]">{blueprint.blueprintId}</Badge>}
                                        </div>
                                        <div className="flex items-center gap-1.5">
                                            {order.printAuthToken && (
                                                <Badge className="bg-emerald-100 text-emerald-700 text-xs flex items-center gap-1">
                                                    <KeyRound className="w-3 h-3" /> Token Issued
                                                </Badge>
                                            )}
                                            <Button
                                                variant="ghost"
                                                size="icon"
                                                className="h-7 w-7"
                                                onClick={() => setViewOrder(order)}
                                            >
                                                <Eye className="w-3.5 h-3.5" />
                                            </Button>
                                        </div>
                                    </div>
                                    <ApprovalStepper order={order} />
                                </div>
                            )
                        })}
                    </div>
                </CardContent>
            </Card>

            {/* Confirm Approval Dialog */}
            <Dialog open={isConfirmOpen} onOpenChange={setIsConfirmOpen}>
                <DialogContent className="max-w-md">
                    <DialogHeader>
                        <DialogTitle className="flex items-center gap-2">
                            {approvingOrder?.type === 'oem'
                                ? <><Building2 className="w-5 h-5 text-purple-600" /> Grant IP License</>
                                : <><Award className="w-5 h-5 text-emerald-600" /> Authorize Print Center</>
                            }
                        </DialogTitle>
                        <DialogDescription>
                            This action will be permanently recorded in the immutable audit log.
                        </DialogDescription>
                    </DialogHeader>
                    {approvingOrderData && (
                        <div className="py-4 space-y-4">
                            <div className="p-4 bg-slate-50 rounded-xl space-y-2">
                                <div className="flex items-center justify-between">
                                    <span className="text-sm font-medium text-slate-500">Order</span>
                                    <span className="font-mono font-bold text-[#0EA5E9]">{approvingOrderData.orderId}</span>
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-sm font-medium text-slate-500">Part</span>
                                    <span className="font-medium text-[#0F172A]">{approvingOrderData.partName}</span>
                                </div>
                                <div className="flex items-center justify-between">
                                    <span className="text-sm font-medium text-slate-500">Quantity</span>
                                    <span className="font-medium text-[#0F172A]">{approvingOrderData.quantity} units</span>
                                </div>
                            </div>
                            <div className={`p-3 rounded-xl text-sm ${approvingOrder?.type === 'oem' ? 'bg-purple-50 text-purple-800' : 'bg-emerald-50 text-emerald-800'
                                }`}>
                                {approvingOrder?.type === 'oem'
                                    ? '⚡ You are granting a one-time IP license. This allows the designated Print Center to decrypt and execute the blueprint exactly once.'
                                    : '⚡ You are verifying that the Print Center holds valid certification. This unlocks the second digital signature required for print authorization.'
                                }
                            </div>
                        </div>
                    )}
                    <DialogFooter>
                        <Button variant="outline" onClick={() => setIsConfirmOpen(false)}>Cancel</Button>
                        <Button
                            onClick={handleConfirmApproval}
                            className={approvingOrder?.type === 'oem'
                                ? 'bg-purple-600 hover:bg-purple-700 text-white'
                                : 'bg-emerald-600 hover:bg-emerald-700 text-white'
                            }
                        >
                            {approvingOrder?.type === 'oem' ? 'Grant IP License' : 'Authorize Print Center'}
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>

            {/* View Pipeline Detail Dialog */}
            <Dialog open={!!viewOrder} onOpenChange={() => setViewOrder(null)}>
                <DialogContent className="max-w-lg">
                    <DialogHeader>
                        <DialogTitle>Approval Pipeline — {viewOrder?.orderId}</DialogTitle>
                    </DialogHeader>
                    {viewOrder && (
                        <div className="space-y-4 py-2">
                            <div className="py-4">
                                <ApprovalStepper order={viewOrder} />
                            </div>
                            <div className="space-y-2">
                                {[
                                    { label: 'Request Submitted', done: true, timestamp: viewOrder.createdAt, by: `Requester` },
                                    { label: 'OEM Approved', done: viewOrder.oemApproval.approved, timestamp: viewOrder.oemApproval.approvedAt, by: viewOrder.oemApproval.approvedBy },
                                    { label: 'Cert Verified', done: viewOrder.certApproval.approved, timestamp: viewOrder.certApproval.approvedAt, by: viewOrder.certApproval.approvedBy },
                                    { label: 'Print Token Issued', done: !!viewOrder.printAuthToken, timestamp: null, by: viewOrder.printAuthToken ? `Token: ${viewOrder.printAuthToken.substring(0, 16)}...` : null },
                                ].map((step, idx) => (
                                    <div key={idx} className={`flex items-center gap-3 p-3 rounded-xl transition-colors ${step.done ? 'bg-emerald-50' : 'bg-slate-50'
                                        }`}>
                                        <div className={`w-6 h-6 rounded-full flex items-center justify-center flex-shrink-0 ${step.done ? 'bg-emerald-500' : 'bg-slate-300'
                                            }`}>
                                            {step.done
                                                ? <CheckCircle2 className="w-3.5 h-3.5 text-white" />
                                                : <Clock className="w-3.5 h-3.5 text-white" />
                                            }
                                        </div>
                                        <div className="flex-1">
                                            <p className={`text-sm font-medium ${step.done ? 'text-[#0F172A]' : 'text-slate-400'}`}>{step.label}</p>
                                            {step.done && step.by && <p className="text-xs text-slate-500">{step.by}</p>}
                                            {step.done && step.timestamp && <p className="text-xs text-slate-400">{new Date(step.timestamp).toLocaleString()}</p>}
                                        </div>
                                        {step.done
                                            ? <Unlock className="w-4 h-4 text-emerald-500 flex-shrink-0" />
                                            : <Lock className="w-4 h-4 text-slate-300 flex-shrink-0" />
                                        }
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}
                </DialogContent>
            </Dialog>
        </div>
    )
}
