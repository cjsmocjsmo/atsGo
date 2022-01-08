FROM golang:bullseye AS builder
RUN mkdir /go/src/atsGo
WORKDIR /go/src/atsGo

COPY atsGo.go .

COPY go.mod .
COPY go.sum .
RUN export GOPATH=/go/src/atsGo
RUN go get -v /go/src/atsGo
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main /go/src/atsGo

FROM alpine:latest
WORKDIR /root/

COPY --from=builder /go/src/atsGo/main .

RUN \
  mkdir ./data && \
  mkdir ./data/db && \
  mkdir ./static && \
  mkdir ./static/images && \
  mkdir ./backups && \
  chmod -R +rwx ./static

COPY static/images/icons/*.svg ./static/images/icons/
COPY static/images/icons/*.png ./static/images/icons/

COPY static/images/*.jpg ./static/images/
COPY static/images/*.webp ./static/images/

COPY static/*.html ./static/
COPY static/*.css ./static/
COPY static/*.js ./static/
COPY static/*.yaml ./static/

COPY backup/*.json ./backups/
COPY backup/*.sh ./backups/

RUN \
  mkdir ./fsData && \
  mkdir ./fsData/thumb && \
  mkdir ./fsData/crap && \
  chmod -R +rwx ./fsData && \
  mkdir ./logs && \
  chmod -R +rwx ./logs

STOPSIGNAL SIGINT
CMD ["./main"]

