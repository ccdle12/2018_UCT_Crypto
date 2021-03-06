'use strict'
/* eslint-disable no-console */

const PeerId = require('peer-id')
const PeerInfo = require('peer-info')
const Node = require('./libp2p-bundle.js')
const pull = require('pull-stream')
const Pushable = require('pull-pushable')
const p = Pushable()

let nodes = new Array()

PeerId.createFromJSON(require('./peer-id-dialer'), (err, idListener) => {
  if (err) {
    throw err
  }
  const peerListener = new PeerInfo(idListener)
  peerListener.multiaddrs.add('/ip4/0.0.0.0/tcp/11323')
  const nodeListener = new Node({
    peerInfo: peerListener
  })

  nodeListener.start((err) => {
    if (err) {
      throw err
    }
    nodeListener.once('peer:discovery', (peerInfo) => {
        nodeListener.dialProtocol(peerInfo,'/chat/1.0.0',(err, conn) => {
            console.log('discovery peer connected')
            console.log('discovery : ' , conn)
          //   pull(
          //     p,
          //     conn
          //   )
      
          //   pull(
          //     conn,
          //     pull.map((data) => {
          //       return data.toString('utf8').replace('\n', '')
          //     }),
          //     pull.drain(console.log)
          //   )
      
    })
    nodeListener.on('peer:connect', (peerInfo) => {
      console.log(peerInfo.id.toB58String())
      // process.stdin.setEncoding('utf8')
      // process.openStdin().on('data', (chunk) => {
      //   var data = chunk.toString()
      //   p.push(data)
      // })
      
      })
    })

    nodeListener.handle('/chat/1.0.0', (protocol, conn) => {
      console.log('protocol' , protocol)
      console.log('handle : ', conn)
      pull(
        p,
        conn
      )

      pull(
        conn,
        pull.map((data) => {
          return data.toString('utf8').replace('\n', '')
        }),
        pull.drain(console.log)
      )

      process.stdin.setEncoding('utf8')
      process.openStdin().on('data', (chunk) => {
        var data = chunk.toString()
        p.push(data)
      })
    })

    console.log('Listener ready, listening on:')
    peerListener.multiaddrs.forEach((ma) => {
      console.log(ma.toString() + '/ipfs/' + idListener.toB58String())
    })
  })
})