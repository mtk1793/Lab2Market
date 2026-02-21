import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then((res) => res.json())

export function useOrders(status?: string, search?: string) {
  const params = new URLSearchParams()
  if (status && status !== 'all') params.append('status', status)
  if (search) params.append('search', search)
  
  const query = params.toString()
  const url = `/api/orders${query ? `?${query}` : ''}`
  
  const { data, error, isLoading, mutate } = useSWR(url, fetcher)
  
  return {
    orders: data || [],
    isLoading,
    isError: error,
    mutate,
  }
}

export function useBlueprints(category?: string, certification?: string, status?: string, search?: string) {
  const params = new URLSearchParams()
  if (category && category !== 'all') params.append('category', category)
  if (certification && certification !== 'all') params.append('certification', certification)
  if (status && status !== 'all') params.append('status', status)
  if (search) params.append('search', search)
  
  const query = params.toString()
  const url = `/api/blueprints${query ? `?${query}` : ''}`
  
  const { data, error, isLoading, mutate } = useSWR(url, fetcher)
  
  return {
    blueprints: data || [],
    isLoading,
    isError: error,
    mutate,
  }
}

export function useCenters() {
  const { data, error, isLoading, mutate } = useSWR('/api/centers', fetcher)
  
  return {
    centers: data || [],
    isLoading,
    isError: error,
    mutate,
  }
}

export function useStats() {
  const { data, error, isLoading, mutate } = useSWR('/api/stats', fetcher)
  
  return {
    stats: data,
    isLoading,
    isError: error,
    mutate,
  }
}

export function useOrder(id: string) {
  const { data, error, isLoading, mutate } = useSWR(id ? `/api/orders/${id}` : null, fetcher)
  
  return {
    order: data,
    isLoading,
    isError: error,
    mutate,
  }
}

export function useBlueprint(id: string) {
  const { data, error, isLoading, mutate } = useSWR(id ? `/api/blueprints/${id}` : null, fetcher)
  
  return {
    blueprint: data,
    isLoading,
    isError: error,
    mutate,
  }
}
