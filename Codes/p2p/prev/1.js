'use strict'
/* eslint-disable no-console */

const PeerId = require('peer-id')
const PeerInfo = require('peer-info')
const Node = require('./libp2p-bundle.js')
const pull = require('pull-stream')
const Pushable = require('pull-pushable')
const p = Pushable()

let connection = new Array()

PeerId.createFromJSON(require('./peer-id-listener'), (err, idListener) => {
  if (err) {
    throw err
  }
  const peerListener = new PeerInfo(idListener)
  peerListener.multiaddrs.add('/ip4/0.0.0.0/tcp/10333')
  const nodeListener = new Node({
    peerInfo: peerListener
  })

  nodeListener.start((err) => {
    if (err) {
      throw err
    }
    nodeListener.on('peer:discovery', (peerInfo) => {
      console.log(connection.conn)
        nodeListener.dialProtocol(peerInfo,'/chat/1.0.0',(err, conn) => {
            console.log('discovery peer connected')
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
      
            // process.stdin.setEncoding('utf8')
            // process.openStdin().on('data', (chunk) => {
            //   var data = chunk.toString()
            //   p.push(data)
            // })
    })
    nodeListener.on('peer:connect', (peerInfo) => {
      console.log(peerInfo.id.toB58String())
      nodeListener.dial(peerInfo, (err,conn) => {
        console.log('redial')
      })
      // process.stdin.setEncoding('utf8')
      // process.openStdin().on('data', (chunk) => {
      //   var data = chunk.toString()
      //   p.push(data)
      // })
      })
    })

    nodeListener.handle('/chat/1.0.0', (protocol, conn) => {
      connection.push(conn)
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