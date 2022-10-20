## First Understanding of Internet and WWW

### Overview 
- The worldwide Internet connected today about more than a billion hosts all over the world
- Security is a key factor for using Internet and WWW.
- Detailed knowledge about Networking, Internet, and Web Technologies is necessary to: 
  - Understand the various security problems occurring in the Internet and WWW.
  - Understand the different threat scenarios and attack methods as well as to develop countermeasures (protection mechanisms).


### Computer Networks

The Internet is a network of computer networks Computer networks consist of:
- Computers: (Can be both or one of the following)
  - Servers - provide services to other computers
  - Clients - make active use of the services provided by servers for their own computing tasks.
- Transmission media: cable or other physical media that connect the computers and intermedia systems.
  - Wired media: e.g. coaxial cable, twisted pair cable, fiber optic cable etc.
  - Wireless media: e.g. radio waves, infrared light, microwaves etc.
- Infrastructure Components:
  - Network Adapter: Transforms computer data into signals that could be transferred over the transmission media.
  - Various network devices: e.g. routers, switches, hubs, bridges, repeaters, gateways, etc. for refrehsing the signal and routing the data to the destination.

Communication within a computer network is organized by Network Protocols that define
- The format of the data to be transmitted
- Address Schema
- Each possible step in the communication process
- Methods for controlling the communication process

### Classification of Computer Networks
Computer networks can be classified according to the following aspects:
- Geographical Scope, Types of Connection, Usage, ...

**Based on Geographical Scope: (Scale)**
| Scope | Type | Example |
| --- | --- | --- |
| 0,1m | Chip/PCB | Multiprocessor System |
| 1m | System | Multiprocessor Cluster |
| 10m | Room | PAN - Personal Area Network |   
| 1km | Building, Campus | LAN - Local Area Network |
| 10km | City | MAN - Metropolitan Area Network |
| 100-1,000km | Land, Continental | WAN - Wide Area Network |
| 10,000km | Planet | Internet |

Difference between **Distributed Systems** and **Computer Networks**:
- Common Properties:
  - Cooperation of many individual computers which are physically and logically different
  - Individual Component's are spatially distributed and operate autonomously, but cooperatively.

- Differences:
  - In distributed systems, the involved component works transparently and is usually managed by a control process. What happens on a component is unavailable for processes at other components as well as for the end users.
  - A computer network is controlled by a network operating system that coordinates the processing steps of a user request.
  
Computer networks can classified along usage criteria:
- Function Sharing Network: Making differenmt functions available at different locations by allowing access to specialized servers (eg. supercomputers, vector computers)

- Load Sharing Networks: Uniform Utilization of Resources by distributing the load among several computers.

- Data Sharing Networks: Better utilization of disks, increased availability of data, and better data security.

- High Reliability Networks: Another system takes over the processing if a computer fails.

... Other Criterias:
Homogeneous vs. Heterogeneous Networks
- Homogeneous Networks: All computers are identical (same shape, type)
- Hetereogeneous Networks: Computers are different (different shapes, types)

Open vs. Private Networks:
- Open Access Networks: All computers can be connected to the network.
- Private Networks: Only authorized computers can be connected to the network.

VPN - Virtual Private Network:
- Internet-based, but behaves as a private netwrok via cryptographic methods.

### Internet and Internet Protocols
As a network of networks the Internet is a virtual computer network:
- Physically, Internet consists of different computer networks that are coupled by means of gateways. (i.e routers)
- The illusion that different network from one homogeneous network is provided by means of the Internet Protocols specifying:
  - How to identify participating computers?
  - Who is the target of the message?
  - How to transmit a message?
  - Which Path through the network of networks should be taken by a message?
  - That messages completely arrive at the destination and free of errors.

- Here's a representation of the such a transfer of a message from one computer to another from Stub Network A1 to Stub Network B2:
```mermaid
graph LR
A[Stub Network A1] --> B[Regional Network A]
B --> C[Backbone Internet]
C --> D[Regional Network B]
D --> E[Stub Network B2]
```

- Communication and networking technologies are typically closed since they are mostly proprietary.
  - Owned by the industry in form of patents or trade secrets ...
- By constrast, the worldwide Internet is an Open System
  - All specifications are publicly available in the form of RFCs (Request for Comments) and any company can build their own techniques based on these standards.
  - All Internet Documentations are online.
- The global Internet has recieved exponential development and great importance during the last two decades, and has proven that open systems in IT work well.

To manage the high complexity of communication over the Internet, Internet Protocols are conceptually organized in heirarchical layers:
There are two famous Layering Models of Communication:
- OSI Reference Model (Open Systems Interconnection)
- TCP/IP Model (Transmission Control Protocol / Internet Protocol)

### TCP/IP Protocol Stack
Layering Model of the TCP/IP Protocol Stack:
```mermaid
graph LR
A[Application Layer] --> B[Transport Layer]
B --> C[Internet Layer]
C --> D[Network Interface Layer]
```
- Network Interface Layer (i.e. Link Layer)
  - Responsible for transporting IP-datagrams over specific networks.
  - The term "Network Interface" tries to suggest the closeness of this layer to the physical network.
  - The core protocols specified by the Internet Engineering Task Force (IETF) are:
    - Address Resolution Protocol (ARP) and its cousin Reverse Address Resolution Protocol (RARP)
    - Neighbor Discovery Protocol (NDP): for delivering similar functionality as ARP for IPv6
    - Layer 2 Tunneling Protocol (L2TP): a tunneling protocol for VPN
    - Media Access Control:
      - Ethernet, DSL, ISDN, FDDI, ...
- Internet Layer
  - Handles communication from one machine to antoher by encapsulating the messages into IP packets, so callewd IP-datagrams. eg. IP
  - It consists of a group of internetworking methods, protocols and specifications, which are used to transmit datagrams (packets) from the originating host to the destination host across multiple IP networks.
  - The core protocols in the Internet Layer are:
    - Internet Protocol (IP): eg, IPv4, IPv6
    - Internet Control Message Protocol (ICMP) and ICMPv6: for error reporting and diagnostic functions
    - Internet Group Managemnet Protocol (IGMP): IPv4 hosts and adjacent multicast routers to establish multicast group memberships.
    - Internet Protocol Security(IPsec): for securing IP traffic via encryption and authentication (cryptography).
  - IPv4 range is not enough for all new devices, eg., Laptops, Smart Phones, Radios, GPS, Cars, TVs, ... online devices.
  - IPv6 range is designed for the future Internet and includes more security features. (eg., mandatory network layer security)
  - We jumped from 2^32 IPv4 addresses to 2^128 IPv6 addresses. To be exact, from around: `4,294,967,296` to `340,282,366,920,938,463,463,374,607,431,768,211,456` unique addresses.
- Transport Layer
  - Provides a universal transport service (end-to-end) communicating application, e.g, TCP, UDP.
  - Offers the service, such as connection-oriented data stream support, reliability, flow control, congestion avoidance and multiplexing (port) etc.
  - The protocols in this layer include:
    - Transmission Control Protocol (TCP): For stateful connections
    - User Datagram Protocol (UDP): For stateless connections
    - Datagram Congestion Control Protocol (DCCP)
    - Stream Control Transmission Protocol (SCTP)
    - Resource Reservation Protocol (RSVP) 
- Application Layer
  - Provides functions and services for programs that want to communicate via the Internet (extends network operation system), e.g., HTTP, FTP, SMTP, POP3, DNS, etc.
  - The protocols in the application layer support network access and offer sevices for user applications (processes), i.e. provide **semantic conventions** between associated application processes.
  - It focuses more on network services, API's, utilites and operating system environments
  - Popular protocol from the applicatio layer: BGP, DHCP, DNS, HTTP, FTP, SMTP, DNS, NMTP, POP, RIP, RTP, SIP, POP/POP3, IMAP,IMAP4, SNMP, SSH, Telnet etc.

### Internet Services and Applications
Internet applications use the services provided in the application layer of the TCP/IP protocol stack.
- Typically, the processes of an application follows the Client/Server-Principal:
  - Client (process) actively requests information or services from the server
  - Server passively waits for such requests and responds with the expected information or services or sends an error messages
- Client and server interact by exchaning messages over the network.

Internet provides various important services:
- File Transfer: eg. FTP
- Naming Services: eg. DNS
- Directory Services: eg. LDAP
- Message Exchange Systems: eg. SMTP, POP3, IMAP
- Internet Chat: eg. IRC
- WWW - World Wide Web: eg. HTTP, HTML, CGI, URL, ...


### WWW - World Wide Web

The World Wide Web (WWW) is a system of interlinked hypertext documents accessed via the Internet. It is the most important Internet Service.
- WWW is an interactive distributed hyper-media system: Multimedia Documents can be easily accessed and exchanged via hyperlinks.
- Thanks to the intuitive graphical user interface (GUI) of browsers, such as Firefox, Chrome, Safari, Internet Explorer, Opera, and WWW can be easily used by everyone.
- WWW was introduced in 1989 by Robert Cailliau and Tim Berners-Lee at CERN (European Organization for Nuclear Research) in Switzerland as a service for Interne-Based Exchange and Administration of Documents.
  
WWW is based on following three basic standards"
- HTML - Hypertext Markup Language
  - specifies format and assembly of hypertext documents "HTML-Documents" from which the Web is built.
- URL - Uniform Resource Locator
  - it is an addressing scheme, which indicates the location of the resource on the Internet as well the protocol to be used to access the resource.
- HTTP - HyperText Transfer Protocol
  - it is the protocol used to access the html-documents on the WWW.

WWW consists of a collection of hundreds of million's documents, which are linked to each other by hyperlinks described in the HyperText Markup Language (HTML).
- A Hypermedia document may consist of different component's
  - Hypertext: text that contains hyperlinks to other parts of the document or to other documents that may even reside on other servers.
  - HyperMedia: audio, graphic, video or other media with hyperlinks.

To access hypermedia documents on the WWW, a unique name is needed for each document. The naming scheme used in WWW is URL
- URL: (Uniform Resource Locator) - identifies a resource by means of
  - The internet name (FQDN or Fully Qualified Domain Name) of the server that hosts the resource.
  - The directory path on the computer, where the resource is located.
  
For transmission of hypermedia documents on the WWW HTTP is used.
- HTTP: (HyperText Transfer Protocol) - is a very simple protocol to access HTML-Documents over the Internet
- HTTP Communication follows a simple request-response-scheme.
- Each data exchange between sender and reciever is completly independent from other data exchanges between these two computers.

Web 2.0: New Behaviour of the WWW
- Web 2.0 is a term used to describe the new behaviour of the WWW, which is based on the following three principles:
  - The WWW is not only a read-only medium, but also a medium for interactive communication.
  - The WWW is not only a medium for static documents, but also a medium for dynamic documents.
  - The WWW is not only a medium for documents, but also a medium for applications.
  - Every user can become a content provider and can publish his own content on the Web 2.0
  - Eg: Blogs, Wikis, Social Networks, Video Sharing, ...
  - Involved technologies: XML, RSS, SOAP, Asynchronous JavaScript and XML (AJAX), etc.

### WWW-Browser and WWW-Server
Client/Server Paradigm is the basic architecture principle of the WWW.
- User requests a document form a Web-Server by means of his/her browser (i.e. the WWW-Client)
- Web-Documents are identified by a URL
- Both, the browser and the server, are programs running on a computer.

Architecture of a WWW-Server:
- Architecture of a browser is much more complex than architecture of a Web-Server
- Beside Communicating with Web-Server the browser has to interpret and display the requested document correctly. To this end it needs to be able to:
  - Open a connection to the Web-Server chosen by the user by activating a hyperlink
  - Recieve the document sent by the Web-Server
  - Interpret, Render and display this document correctly.
  - React on actions (eg. mouse clicks) of the user on the GUI.

Architecture of a Browser:
- In order to able to fulfill all these tasks a web brwoser consists of various clients, interpreter and one controller
- Controller supervises all browser functions and interprets mouse-clicks of the user.
- HTML-Interpreter is needed to interpret the HTML-Document from a vast majority of resouces on the WWW.
- Nowadays, various other Internet Services can be accessed by means of a browser. The browser has been a standard/Widely accepted service client.
- To Increase efficieny, browsers use caches for parking visted pages.


### History of Internet and WWW

1960 - Idea of Packet Switching
- Idea of packet switching was first proposed by Donald Davies in 1960. The idea was to divide a message into small packets and to route them independently through the network. In simple terms, it basically means to fragment the data into different peices and send them to the reciever, who puts all these peices together to form the original data.

1967 - start of ARPANET-project
- The ARPANET was the first network to implment such an idea.

1969 - ARPANET goes online with 4 nodes, three in California and one in Denver.
1970 - Start of the radio network ALOHANET connecting four Hawaiian islands.
1971 - First Email was sent.
1973 - ARPANET has 35 nodes.
- Vinton Cerf and Robert Kahn developed the TCP/IP-Protocol Suite, which is still the most important protocol suite for the Internet.
1983 - ARPANET switches over to TCP/IP-Protocol and the birth of the Internet.
1986 - Start of NSFNET, the first national backbone of the Internet, a high speed network.
1988 - First Internet worm disturbs 10% of the whole Internet hosts - at that time about 60,000 hosts.
1989 - Internet connects 150,000 hosts.
1990 - Robert Cailliau and Tim Berners-Lee introduce the World Wide Web (WWW) at CERN.
1993 - NCSA Mosaic offers first WWW-Browser with Graphical User Interface (GUI). Netscape.
1994 - Netscape and World Wide Web Consortium (W3C) was founded.
1995 - Microsfot offers Windows 95 with Internet Explorer.
1997 - 2000 - Dotcom bubble.
2005 - 2012 - Web 3.0 
- Semantic Web, Service Web, Social Web: a different way to use Internet, new sevices like Google, Facebook, Twitter, Youtube etc.
- Feb 03 2011: All the IPv4 addressses have been assinged (Problem: IPv4 addresses are limited)

### Who is Who in the Internet

There is no central authority in the Internet. It is a collobrative effort of many different organizations, nations and individuals.
- Internet Architecture Board (IAB) - is a group of experts, which is responsible for the development of the Internet Architecture.
- IAB has a RFC-editor and consits of about 10 so-called Internet Task Forces (ITF), which are responsible for the certain problems of the Internet.
- Two most important ITFs are:
  - Internet Research Task Force (IRTF)
  - Internet Engineering Task Force (IETF): which co-ordinates research and development of the Internet.
- Internet Assigned Numbers Authority (IANA) - originally responsible for the allocation of IP-Addresses and other Internet Numbers.
- Nowadays, this is done by Internet Corporation for Assigned Names and Numbers (ICANN).
- In 1992, the international non-profit organization Internet Society (ISOC) was founded, which is responsible for the development of the Internet.
- IAB has become a part of ISOC.

### Internet Standards
The success of the Internet and WWW is based on the use of open standards. How the Internet Standards are defined:
- Standardization in the Internet is a cooperative process of all the above mentioned organizations.
- TCP/IP technology is open and not proprietary. Everyone can learn it, use it and develop it.
- All standards are published in the form of RFCs (Request for Comments) online for free.
- Nothing can became a standard without practical implementation.

Standardization is done by so-called Request for Comments (RFCs) - published by IESG (Internet Engineering Steering Group) which consists of IETF Chair and Area Directors or IAB
- Starting point of a standarziation is an Internal Draft
- After Permission of IESG it is published (unchanged or changed) as RFC-Draft Standard if:
  - At Least 6 months discussion in the whole implementation in the whole Internet community
  - if at lease two indendent implementations have been proven to work well.
- Draft standards can became a Internet Offical Protocol Standard.

# Resources

The following are the resources: 
- [Lecture Video](https://www.tele-task.de/lecture/video/7084/)
- Professor Dr. Christoph Meinel
- Notes Author: [@is-it-ayush](https://github.com/is-it-ayush)