const readline = require('readline')
const Room = require('ipfs-pubsub-room')
const IPFS = require('ipfs')
const ipfs = new IPFS({
  EXPERIMENTAL: {
    pubsub: true
  },
  config: {
    Addresses: {
      Swarm: [
        '/dns4/ws-star.discovery.libp2p.io/tcp/443/wss/p2p-websocket-star'
      ]
    }
  }
})
// IPFS node is ready, so we can start using ipfs-pubsub-room
ipfs.on('ready', () => {
  const room = Room(ipfs, 'testing')

//   console.log(id)
  function send(data){
      room.broadcast(data)
  }

  const r1 = readline.createInterface({
      input:process.stdin,
      output:process.stdout
  })
  
  r1.on("line", (data) => {
    send(data)
  })

  room.on('peer joined', (peer) => {
    console.log('Peer joined the room', peer)
    room.sendTo(peer, 'Heewon - Welcome :)')
  })

  room.on('peer left', (peer) => {
    console.log('Peer left...', peer)
  })
  
  // now started to listen to room
  room.on('subscribed', () => {
    console.log('Now connected!')
    
  })
  
  room.on('message', (message) => {
    msgsender = message.from
    // console.log(msgsender)
    ipfs.id((err, identity) => {
        if(err) throw err;
        id = identity.id
        if(msgsender != id)
            console.log(message.data.toString('utf8'))    
    })
  })
})