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
  mkdir ./static/images/kitsappics && \
  mkdir ./static/images/masonpics && \
  mkdir ./static/images/piercepics && \
  mkdir ./backup

COPY backup/*.json ./backup/
COPY backup/*.gz ./backup/
COPY static/images/*.webp ./static/images/
COPY static/images/kitsappics/ ./static/images/kitsappics/
COPY static/images/masonpics/ ./static/images/masonpics/
COPY static/images/piercepics/ ./static/images/piercepics/
COPY static/*.html ./static/
COPY static/*.css ./static/
COPY static/*.js ./static/
COPY static/*.yaml ./static/
RUN chmod -R +rwx ./static


RUN \
  mkdir ./fsData && \
  mkdir ./fsData/thumb && \
  mkdir ./fsData/crap && \
  chmod -R +rwx ./fsData && \
  mkdir ./logs && \
  chmod -R +rwx ./logs && \
  chmod -R +rwx ./backup

STOPSIGNAL SIGINT
CMD ["./main"]

