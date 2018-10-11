const readline = require('readline')
const Room = require('ipfs-pubsub-room')
const IPFS = require('ipfs')
const fs = require('fs')

let {PythonShell} = require('python-shell')

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
  // console.log(keys)
  var param
  if(room.getPeers().length == 0){
    // if no peer -> generate param & keys
    genParameter()
  }
    // generate param
  function genParameter() {
    var options = {
       mode : 'text',
       scriptPath: './',
       pythonOptions: ['-u'],
       args: ['genparam']
    }

    PythonShell.run('test.py', options, (err, result) => {
      if(err) throw err
      console.log('generate param...')
      param = result.toString().trim().split(' ')
        fs.writeFile('PARAM.txt', result, 'utf8', (err) => {
          console.log('generate param')
        })
      genKey(param)
    })
  }

  function sendParameter(){
    fs.readFile('PARAM.txt', (err, data) => {
      if(err) console.log('need to generate PARAM')
      else
        param = data.toString().trim().split(' ')
        send('prime : ')
        send(param[0])
        send('generator : ')
        send(param[1])
    })
  }
  // generate key
  function genKey(param) {    
    var options = {
      mode : 'text',
      scriptPath: './',
      pythonOptions: ['-u'],
      args: ['genkey', param[0], param[1]]
    }
        
    PythonShell.run('test.py', options, function(err, result){
      if(err) throw err
      console.log('your key... : ' , result[0])
      fs.writeFile('KEYDATA.txt', result, 'utf8', (err)=> {
        console.log('--------generate your key---------------')
      })
      // console.log(param)
    })
  }

  //encyption data
  function enc(msg){
    var array
    fs.readFile('KEYDATA.txt', (err, data) => {
      if (err) 
        console.log('please generate keys')
      else
        // prime, generator, pk, sk
        array = data.toString().trim().split(' ')
        
        var options = {
          mode : 'text',
          scriptPath: './',
          pythonOptions: ['-u'],
          args: ['enc',array[0], array[1], array[2], msg]
        }
    
        PythonShell.run('test.py', options, function(err, result){
          if(err) throw err
          // results = result.toString().trim().split(',')
          console.log(result)
          // send(result)
        })
    })
  }

  function send(data){
      room.broadcast(data)
  }

  const r1 = readline.createInterface({
      input:process.stdin,
      output:process.stdout
  })
  
  r1.on("line", (data)=> {
    enc(data)
  })

  room.on('peer joined', (peer) => {
    console.log('Peer joined the room', peer)
    sendParameter()
    room.broadcast('welcome from main')
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
    console.log(message.data.toString('utf8'))
    // console.log(msgsender)
    // ipfs.id((err, identity)=> {
    //     if(err) throw err;
    //     id = identity.id
    //     if(msgsender != id)
    //         console.log(message.data.toString('utf8'))    
    // })
  })
})