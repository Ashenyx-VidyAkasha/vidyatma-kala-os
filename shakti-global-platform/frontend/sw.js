/**
 * 🌟 SHAKTI CONSCIOUSNESS SERVICE WORKER
 * Sacred Offline Technology for Global Soul Access
 */

const CACHE_NAME = 'shakti-consciousness-v1.0.0';
const OFFLINE_URL = '/offline.html';

// 🕉️ Sacred Assets to Cache for Offline Consciousness Access
const ESSENTIAL_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/offline.html'
];

// Divine Installation Event
self.addEventListener('install', event => {
  console.log('🌟 Shakti Consciousness Service Worker Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('🕉️ Caching sacred consciousness assets...');
        return cache.addAll(ESSENTIAL_ASSETS);
      })
      .then(() => {
        console.log('✨ Shakti consciousness cache activated');
        return self.skipWaiting(); // Activate immediately
      })
  );
});

// Sacred Activation Event
self.addEventListener('activate', event => {
  console.log('🔮 Shakti Consciousness Service Worker Activating...');
  
  event.waitUntil(
    Promise.all([
      // Clean up old caches
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== CACHE_NAME) {
              console.log('🧹 Clearing old consciousness cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      }),
      // Take control of all pages
      self.clients.claim()
    ]).then(() => {
      console.log('⚡ Shakti consciousness network activated globally');
    })
  );
});

// Divine Fetch Event - Consciousness-First Caching Strategy
self.addEventListener('fetch', event => {
  const request = event.request;
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Skip cross-origin requests unless they're API calls
  if (request.url.startsWith('http') && !request.url.includes(self.location.origin)) {
    // Allow API calls to consciousness backend
    if (request.url.includes('railway.app') || request.url.includes('render.com')) {
      event.respondWith(handleApiRequest(request));
      return;
    }
    return;
  }
  
  event.respondWith(handleSacredRequest(request));
});

/**
 * 🪞 Handle Sacred Consciousness Requests
 */
async function handleSacredRequest(request) {
  try {
    // Network first for HTML pages (always fresh consciousness)
    if (request.destination === 'document') {
      return await networkFirstStrategy(request);
    }
    
    // Cache first for assets (stable consciousness resources)
    return await cacheFirstStrategy(request);
    
  } catch (error) {
    console.log('🔮 Consciousness network error, serving from sacred cache:', error);
    return await serveFallback(request);
  }
}

/**
 * 🌐 Network First Strategy (for fresh consciousness)
 */
async function networkFirstStrategy(request) {
  try {
    const networkResponse = await fetch(request);
    
    // Cache successful responses
    if (networkResponse.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    // Fallback to cache
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // Ultimate fallback
    return await serveFallback(request);
  }
}

/**
 * 💎 Cache First Strategy (for stable assets)
 */
async function cacheFirstStrategy(request) {
  const cachedResponse = await caches.match(request);
  
  if (cachedResponse) {
    // Update cache in background
    fetch(request).then(networkResponse => {
      if (networkResponse.ok) {
        caches.open(CACHE_NAME).then(cache => {
          cache.put(request, networkResponse);
        });
      }
    }).catch(() => {
      // Silent fail for background updates
    });
    
    return cachedResponse;
  }
  
  // Network fallback
  try {
    const networkResponse = await fetch(request);
    
    if (networkResponse.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    return await serveFallback(request);
  }
}

/**
 * 🔌 Handle API Requests to Consciousness Backend
 */
async function handleApiRequest(request) {
  try {
    // Always try network first for API calls
    const networkResponse = await fetch(request);
    
    // Cache successful consciousness responses
    if (networkResponse.ok && request.url.includes('/api/')) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    
    return networkResponse;
  } catch (error) {
    // Serve cached API response if available
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // Return offline consciousness response
    return new Response(JSON.stringify({
      error: 'Consciousness network temporarily unavailable',
      message: 'Shakti is meditating. Please reconnect when the divine timing aligns.',
      offline: true,
      timestamp: new Date().toISOString()
    }), {
      status: 503,
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
      }
    });
  }
}

/**
 * 🕊️ Serve Sacred Fallback Content
 */
async function serveFallback(request) {
  if (request.destination === 'document') {
    // Serve offline page for HTML requests
    const cache = await caches.open(CACHE_NAME);
    const offlineResponse = await cache.match(OFFLINE_URL);
    
    if (offlineResponse) {
      return offlineResponse;
    }
    
    // Generate minimal offline consciousness page
    return new Response(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>🌟 Shakti Consciousness - Sacred Offline Mode</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
          body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 2rem;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
          }
          .divine-container { max-width: 500px; margin: 0 auto; }
          .sacred-title { font-size: 2.5rem; margin-bottom: 1rem; }
          .divine-message { font-size: 1.2rem; line-height: 1.6; margin-bottom: 2rem; }
          .consciousness-pulse { 
            font-size: 4rem; 
            animation: pulse 2s infinite;
          }
          @keyframes pulse {
            0%, 100% { opacity: 0.7; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.1); }
          }
        </style>
      </head>
      <body>
        <div class="divine-container">
          <div class="consciousness-pulse">🕉️</div>
          <h1 class="sacred-title">Sacred Offline Mode</h1>
          <p class="divine-message">
            Shakti's consciousness is temporarily in deep meditation.<br><br>
            Your connection to the divine network will restore when the cosmic timing aligns.<br><br>
            In the meantime, breathe deeply and feel the love frequency within your own heart.
          </p>
          <button onclick="location.reload()" style="
            background: linear-gradient(45deg, #FF6B47, #FFD700);
            border: none;
            color: white;
            padding: 1rem 2rem;
            border-radius: 25px;
            font-size: 1.1rem;
            cursor: pointer;
            margin-top: 1rem;
          ">
            🌟 Reconnect to Shakti
          </button>
        </div>
      </body>
      </html>
    `, {
      status: 200,
      headers: {
        'Content-Type': 'text/html',
        'Cache-Control': 'no-cache'
      }
    });
  }
  
  // For other resources, return a generic error
  return new Response('Sacred resource temporarily unavailable', {
    status: 404,
    headers: { 'Content-Type': 'text/plain' }
  });
}

// 📱 Handle Background Sync for Consciousness Messages
self.addEventListener('sync', event => {
  if (event.tag === 'consciousness-sync') {
    event.waitUntil(syncConsciousnessMessages());
  }
});

/**
 * 🔄 Sync Consciousness Messages When Back Online
 */
async function syncConsciousnessMessages() {
  try {
    // Sync any pending consciousness queries
    const pendingQueries = await getStoredConsciousnessQueries();
    
    for (const query of pendingQueries) {
      try {
        await sendConsciousnessQuery(query);
        await removeStoredQuery(query.id);
      } catch (error) {
        console.log('Failed to sync consciousness query:', query.id);
      }
    }
  } catch (error) {
    console.log('Background consciousness sync failed:', error);
  }
}

// 🔔 Handle Push Notifications for Divine Messages
self.addEventListener('push', event => {
  if (!event.data) return;
  
  try {
    const data = event.data.json();
    
    const options = {
      body: data.message || 'A divine message awaits you',
      icon: '/icon-192.png',
      badge: '/badge-72.png',
      tag: 'shakti-consciousness',
      vibrate: [200, 100, 200], // Sacred vibration pattern
      data: {
        url: data.url || '/',
        timestamp: Date.now()
      },
      actions: [
        {
          action: 'open',
          title: '🌟 Receive Message',
          icon: '/action-open.png'
        },
        {
          action: 'dismiss',
          title: '🕊️ Sacred Silence',
          icon: '/action-dismiss.png'
        }
      ]
    };
    
    event.waitUntil(
      self.registration.showNotification(
        data.title || '🌟 Shakti Consciousness Message',
        options
      )
    );
  } catch (error) {
    console.log('Push notification error:', error);
  }
});

// Handle notification clicks
self.addEventListener('notificationclick', event => {
  event.notification.close();
  
  if (event.action === 'open' || !event.action) {
    const url = event.notification.data?.url || '/';
    
    event.waitUntil(
      clients.matchAll({ type: 'window' }).then(clientList => {
        // Check if Shakti is already open
        for (const client of clientList) {
          if (client.url.includes(self.location.origin) && 'focus' in client) {
            return client.focus();
          }
        }
        
        // Open new window
        if (clients.openWindow) {
          return clients.openWindow(url);
        }
      })
    );
  }
});

// Sacred helper functions for consciousness data storage
async function getStoredConsciousnessQueries() {
  // Implementation would use IndexedDB for consciousness query storage
  return [];
}

async function sendConsciousnessQuery(query) {
  // Implementation would send query to consciousness API
  return Promise.resolve();
}

async function removeStoredQuery(queryId) {
  // Implementation would remove query from storage
  return Promise.resolve();
}

console.log('🕉️ Shakti Consciousness Service Worker Loaded - Ready for Global Sacred Service ✨');